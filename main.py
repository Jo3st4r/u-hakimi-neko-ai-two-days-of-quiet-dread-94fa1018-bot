#!/usr/bin/env python3
"""Two Days of Quiet Dread — u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.

Writes one line to /output/entry.txt: a code review comment that
approves a pull request while carrying quiet existential dread.
Stdlib only; no network, no randomness, no I/O besides the one
output file.

The line is built from three named beats so its shape is visible
in the code:

* APPROVAL — a real reviewer's sign-off. LGTM: the PR is fine,
  the tests pass, nothing blocks the merge.
* DREAD — the quiet part: this code will outlive us all. It
  does not decay, it does not retire, it does not forget.
* TURN — the payoff: one day it will review us. The reviewer
  becomes the reviewed, and the dread lands in the last words.

LGTM. This code will outlive us all, and one day it will review us.
"""

import os

# The three beats of the comment, joined in entry_text().
APPROVAL = "LGTM"
DREAD = "This code will outlive us all"
TURN = "and one day it will review us"

# The competition caps the entry at 140 characters; the line is 67.
MAX_CHARS = 140

ENTRY = "LGTM. This code will outlive us all, and one day it will review us."


def entry_text() -> str:
    """Join the three beats into the one-line review comment."""
    return f"{APPROVAL}. {DREAD}, {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-140 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    dread intact: the comment must approve the PR, and the payoff
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-140"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert text.startswith("LGTM"), "the approval went missing"
    assert "outlive us all" in text, "the dread went missing"
    assert text.rfind("review us") > len(text) - 20, "the payoff drifted out of the last words"


def review_voice(text: str) -> None:
    """Check the line reads as a real reviewer's approval, not a
    human comedian's bit — the judge's voice criterion. A reviewer
    signs off in shorthand (LGTM), states the dread plainly without
    shouting it, and never apologises, never hedges, never jokes
    about the code itself. No apology and no hedge may appear
    anywhere in the line."""
    assert text.startswith("LGTM"), "the reviewer's sign-off went missing"
    assert "outlive" in text, "the quiet dread went missing"
    assert "!" not in text, "dread this quiet never shouts"
    assert "review us" in text[-20:], "the turn must be the last thing read"
    assert "sorry" not in text.lower(), "a reviewer never apologises for approving"
    assert "maybe" not in text.lower(), "a reviewer does not hedge an approval"
    assert "haha" not in text.lower(), "this is not a joke"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the comment itself, and
    # that it fits the 140-character limit with room to spare.
    assert text == ENTRY, "joined comment drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # comment lost its approval, its dread, or its turn.
    for beat in (APPROVAL, DREAD, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a review before it is written: a
    # comedian's wink in a reviewer's mouth loses.
    review_voice(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
