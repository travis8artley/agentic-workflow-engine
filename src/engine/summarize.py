def summarize(results: list[dict]) -> dict:
    completed = sum(1 for r in results if r.get("status") == "completed")
    failed = sum(1 for r in results if r.get("status") == "failed")
    return {"completed": completed, "failed": failed, "total": len(results)}
