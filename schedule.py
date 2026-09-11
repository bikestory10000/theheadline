#!/usr/bin/env python3
"""발행 큐. queue.json = [{"json":"data/NEWS_WORD_001.json","date":"2026-09-15","done":false}, ...]
  python queue.py pick            → 오늘(KST) 날짜의 미발행 항목 1개 출력 (json=...)
  python queue.py done <path>     → 발행 완료 표시
  python queue.py add <path> <YYYY-MM-DD>"""
import json, sys, pathlib, datetime
Q = pathlib.Path("queue.json"); q = json.loads(Q.read_text()) if Q.exists() else []
cmd = sys.argv[1] if len(sys.argv) > 1 else "pick"
kst = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).date().isoformat()
if cmd == "pick":
    for it in q:
        if not it.get("done") and it.get("date", kst) <= kst:
            print(f"json={it['json']}"); break
    else:
        print("json="); print("오늘 발행할 항목 없음", file=sys.stderr); sys.exit(78)  # neutral exit → 워크플로 중단
elif cmd == "done":
    for it in q:
        if it["json"] == sys.argv[2]: it["done"] = True
    Q.write_text(json.dumps(q, ensure_ascii=False, indent=2))
elif cmd == "add":
    q.append({"json": sys.argv[2], "date": sys.argv[3], "done": False})
    Q.write_text(json.dumps(q, ensure_ascii=False, indent=2))
