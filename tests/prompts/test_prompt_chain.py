"""Tests for PromptChain and argument substitution."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from app.prompts.load import load_prompt_template, PromptChain, load_prompt


def test_argument_injection() -> None:
    msgs = load_prompt_template("variance_dm", summary="Test summary")
    assert any("Test summary" in m.content.text for m in msgs)


def test_chain_run() -> None:
    data = "Sample variance"
    chain = PromptChain(load_prompt("variance_workflow")["steps"])
    msgs = chain.run(data=data)
    assert any("Sample variance" in m.content.text for m in msgs)
