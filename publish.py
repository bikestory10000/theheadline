#!/usr/bin/env python3
"""
캐러셀 발행 (Instagram API with Instagram Login)
사용:
  export IG_USER_ID=17841428545104984
  export IG_ACCESS_TOKEN=IGAAP...
  export BASE_URL=https://bikestory10000.github.io/theheadline/png
  python3 publish.py data/NEWS_IDIOM_001.json            # 실제 발행
  python3 publish.py data/NEWS_IDIOM_001.json --dry-run  # URL 검사 + 캡션만 출력
"""
import json, os, sys, time, glob, pathlib, urllib.request, urllib.parse

API = "https://graph.instagram.com/v23.0"
IG_USER = os.environ.get("IG_USER_ID")
TOKEN = os.environ.get("IG_ACCESS_TOKEN")
BASE = os.environ.get("BASE_URL", "").rstrip("/")
DRY = "--dry-run" in sys.argv
SRC = pathlib.Path([a for a in sys.argv[1:] if not a.startswith("--")][0])
D = json.loads(SRC.read_text(encoding="utf-8"))

def post(path, data):
    body = urllib.parse.urlencode({**data, "access_token": TOKEN}).encode()
    req = urllib.request.Request(f"{API}/{path}", data=body, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)

def get(path, params):
    q = urllib.parse.urlencode({**params, "access_token": TOKEN})
    with urllib.request.urlopen(f"{API}/{path}?{q}", timeout=60) as r: return json.load(r)

def head_ok(url):
    try:
        req = urllib.request.Request(url, method="HEAD")
        return urllib.request.urlopen(req, timeout=20).status == 200
    except Exception as ex:
        print("   ✗", url, ex); return False

def wait_finished(cid, label):
    for _ in range(30):
        s = get(cid, {"fields": "status_code,status"})
        if s.get("status_code") == "FINISHED": return
        if s.get("status_code") == "ERROR": raise SystemExit(f"컨테이너 오류 {label}: {s}")
        time.sleep(3)
    raise SystemExit(f"컨테이너 대기 시간 초과 {label}")

# ---------- 캡션 ----------
def caption():
    if D.get("kind") == "weekly":
        items = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in D["items"]]
        ans = [f"{i+1}. {x['quiz_options']['ABCD'.index(x['quiz_answer'])]}" for i, x in enumerate(items)]
        return "\n".join([f"이번 주 표현 {len(items)}개, 한 장으로 ({D['week']})", "",
            *[f"{x['number']} {x['expression']} = {x['meaning_ko']}" for x in items], "",
            "2장 복습 퀴즈 정답: " + " / ".join(ans), "",
            "놓친 편은 프로필 고정 게시물에서.", "",
            "#외신영어 #헤드라인영어 #뉴스영어 #영어표현 #편입영어 #영어공부 #주간정리"])
    lines = [D['hook_ko'], "",
             f"{D['source']} — “{D['headline']}”",
             D['news_summary_ko'], "",
             f"{D['expression']} = {D['meaning_ko']}",
             D['example_work_en'], "",
             f"퀴즈 정답은 {D['quiz_answer']}. 몇 번 골랐는지 댓글로 남겨주세요.",
             "이 시리즈 전체 목록은 프로필 고정 게시물에.", "",
             " ".join(D['hashtags'])]
    return "\n".join(lines)

# ---------- 이미지 목록 ----------
tag = D['id']
files = sorted(pathlib.Path("png").glob(f"{tag}_card_0?.png"))
if not files: raise SystemExit("png/ 에 렌더된 카드가 없습니다. render.py 먼저.")
if len(files) > 10: raise SystemExit(f"캐러셀은 API 기준 10장 최대. 현재 {len(files)}장")
if len(files) < 2: raise SystemExit("캐러셀은 2장 이상")
urls = [f"{BASE}/{f.name}" for f in files]

print(f"[{D['id']}] {len(files)}장")
print("1) 공개 URL 검사 (Pages 배포 대기, 최대 6분)")
for attempt in range(24):
    if all(head_ok(u) for u in urls): break
    print(f"   … 아직 배포 전, 15초 후 재시도 ({attempt+1}/24)"); time.sleep(15)
else:
    raise SystemExit("6분 내 이미지가 공개되지 않았습니다. Pages 설정을 확인하세요.")
for u in urls: print("   ·", u)

print("\n2) 캡션\n" + "-"*40 + "\n" + caption() + "\n" + "-"*40)
if DRY:
    print("\n(dry-run) 여기서 멈춤."); sys.exit(0)
if not (IG_USER and TOKEN): raise SystemExit("IG_USER_ID / IG_ACCESS_TOKEN 환경변수 필요")

print("\n3) 자식 컨테이너 생성")
children = []
for u, f in zip(urls, files):
    r = post(f"{IG_USER}/media", {"image_url": u, "is_carousel_item": "true"})
    children.append(r["id"]); print("   ·", f.name, "→", r["id"])
for cid in children: wait_finished(cid, cid)

print("4) 부모 컨테이너 생성")
parent = post(f"{IG_USER}/media", {"media_type": "CAROUSEL", "children": ",".join(children), "caption": caption()})
wait_finished(parent["id"], "parent")

print("5) 발행")
res = post(f"{IG_USER}/media_publish", {"creation_id": parent["id"]})
print("✓ 발행 완료. media id:", res.get("id"))

# 발행 기록
log = pathlib.Path("published.json")
hist = json.loads(log.read_text()) if log.exists() else []
hist.append({"id": D['id'], "media_id": res.get("id"), "at": time.strftime("%Y-%m-%d %H:%M"), "cards": len(files)})
log.write_text(json.dumps(hist, ensure_ascii=False, indent=2))
