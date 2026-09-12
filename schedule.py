#!/usr/bin/env python3
"""발행 큐.
  python schedule.py pick        → 오늘(KST) 미발행 항목 1건 (없으면 json= 빈값, 정상 종료)
  python schedule.py done <path> → 발행 완료 표시
  python schedule.py add <path> <YYYY-MM-DD>"""
import json, sys, pathlib, datetime

Q = pathlib.Path("queue.json")
q = json.loads(Q.read_text(encoding="utf-8")) if Q.exists() else []
cmd = sys.argv[1] if len(sys.argv) > 1 else "pick"
kst = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)).date().isoformat()

if cmd == "pick":
    for it in q:
        if not it.get("done") and it.get("date", kst) <= kst:
            print(f"json={it['json']}")
            break
    else:
        print("json=")
        print(f"오늘({kst}) 발행할 항목 없음 — 정상 종료", file=sys.stderr)

elif cmd == "done":
    for it in q:
        if it["json"] == sys.argv[2]:
            it["done"] = True
    Q.write_text(json.dumps(q, ensure_ascii=False, indent=2), encoding="utf-8")

elif cmd == "add":
    q.append({"json": sys.argv[2], "date": sys.argv[3], "done": False})
    Q.write_text(json.dumps(q, ensure_ascii=False, indent=2), encoding="utf-8")
