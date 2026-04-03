from src.engine.orchestrator import run


def test_orchestrator_summary_counts_tasks():
    output = run("demo goal")
    assert output["summary"]["total"] == 2
    assert output["summary"]["completed"] == 2
    assert output["summary"]["failed"] == 0
