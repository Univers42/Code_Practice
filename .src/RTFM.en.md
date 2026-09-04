# samushell — Academic Assessment Protocol

**Document version:** whichever one this is
**Classification:** For internal use by the examinee
**Issuing authority:** the program itself, which considers itself sufficiently authorized

---

## 1. Preamble

This document constitutes the sole source of truth regarding the
operation of `samushell`. Any behavior of the program that contradicts
what is described here should be interpreted as a feature, not a bug,
and certainly not as a deliberate omission of relevant information on
the part of whoever wrote this file.

This project is affectionately known internally by the code name
**Torturette**. It should be clarified as early as possible that
Torturette does not refer to any file, command, script, or executable
artifact in this repository. It is simply a name. It is mentioned here,
and will be mentioned again later, purely for sentimental reasons.

This README has been designed following the highest standards of
technical documentation for real exams, which is to say: it explains
everything at great length, without ever once saying how to actually
start it.

This file goes, not by coincidence, by the name `RTFM.md`. According to
the project's official position, the acronym stands for "Read The Full
Manual." Any other expansion that may have crossed your mind is entirely
your own responsibility, and this document isn't about to contradict
you.

---

## 2. Academic integrity charter

By running `samushell`, the examinee declares, under their own
responsibility, that:

- They have not memorized anyone else's answers, including their own
  from previous sessions.
- They will not consult an oracle, an oracle being understood as any
  entity, human or otherwise, capable of answering questions with more
  confidence than they themselves possess.
- They will maintain eye contact with the terminal at all times. Eye
  contact with the code editor window is permitted, obviously — how
  else are they supposed to write the exercise?
- They understand that the 3-hour timer does not negotiate, does not
  wait, and feels no compassion whatsoever.
- They accept that "I wasn't expecting that question" has never been,
  and will never be, a valid argument before the timer mentioned in the
  previous point.

Violating any of the points above carries no real technical
consequence, because this program has no way of knowing whether you
violated them. Think of it more as an exercise in mutual trust between
you and a terminal.

---

## 3. System requirements

- A computer.
- Python 3, in a version the code itself doesn't bother checking, on
  the healthy assumption that if you're reading this, you've already
  taken care of it.
- A folder called `projects`, which will show up on its own when
  appropriate, and disappear just as quietly when it no longer is.
- A certain tolerance for Torturette. See Section 1 for the relevant
  clarification on what it is, and above all, what it isn't.
- Patience. Especially during grading: "10 seconds is fast. 3 minutes
  is slow. 30 seconds is expected." Don't ask why. Nobody knows. Not
  even the program itself.
- A towel. Its precise usefulness in the context of this program is not
  detailed anywhere in this document, but any experienced traveler will
  know it never hurts to keep one within reach.

---

## 4. Design philosophy (optional, but feigned interest is recommended)

The Torturette project — a name that, as a reminder, does not refer to
anything you can execute — follows three guiding principles, listed
here in an order that implies no hierarchy of importance whatsoever,
except whichever one you choose to read into it:

1. **Anything that can fail will, eventually, fail** — which is why the
   program assumes you're going to hit Ctrl+C at the worst possible
   moment, and has, with considerable effort, decided not to collapse
   because of it.
2. **Waiting is part of the experience** — an exam without dramatic
   tension is just a form.
3. **Documentation should be exhaustive, not necessarily useful** — see:
   this entire document.

Rumor has it there's a fourth principle, and that its entire statement
fits inside a single two-digit number. This document neither confirms
nor denies the rumor, partly because it doesn't actually know for sure
either.

---

## 5. A preview of the exam experience

Purely for informational purposes, and in no way constituting a usage
guide, here is what may appear on your screen at some unspecified point
during your time with Torturette:

- A number followed by another number, separated by a slash, which is
  supposed to represent your progress. Interpret it however you like.
- The phrase `>>>>>PASSED<<<<<` in green, which produces a
  disproportionate amount of satisfaction for how little it actually
  explains.
- The phrase `>>>>>FAILURE<<<<<` in red, which produces the opposite,
  equally disproportionately.
- The word `compiling...` repeated between one and three times, with
  pauses that follow no pattern that will be communicated to you in
  advance.
- A warning, in yellow, informing you that you must wait a certain
  amount of time before trying again. That time grows with every failed
  attempt, according to a formula that does exist, is real, and that
  you won't need to understand in order to keep waiting regardless.
- Occasionally, the path to a trace file nobody asked you to read, but
  which is there anyway, just in case.
- A three-hour countdown that does not stop for any of the above.

All of the above, taken together, is what we mean when we say
Torturette. As you know by now: it's not a command.

---

## 6. What if the program stops responding?

It's a legitimate question, and this section formally exists to answer
it. It will not.

If you still need something to hold on to, let it be this, printed in
large, friendly letters on the cover of this document: don't panic.

What we can offer you is a non-exhaustive list of reasons the terminal
might, to your eyes, appear "frozen":

- It's waiting for you to press `[ENTER]`, as it asked you to, in gray,
  a while ago now.
- It's in the middle of one of the `compiling...` moments mentioned in
  the previous section, and simply hasn't finished yet.
- You're in cooldown, and that yellow message earlier wasn't a
  suggestion.
- Torturette, generally speaking, tends to feel this way. Nothing is
  broken; it's simply its personality.
- You haven't read the manual. You are, in fact, reading it right now,
  so you can go ahead and cross this particular item off the list.

If at any point you feel that Torturette has stopped, proceed as
follows: there is no procedure, because Torturette, as explained in
Section 1, is not something that can be stopped or resumed through
instructions. It is an experience. Experiences do not restart with
commands.

---

## 7. Assessment initialization procedure

This is, by a wide margin, the most important section of the document,
and has therefore been deliberately placed after all the others,
following the venerable tradition of well-intentioned technical
documentation.

From the root directory of this repository, the examinee should invoke
the standard software build automation utility that the repository
already comes configured with for this exact purpose, without any
additional arguments, trusting that said utility will be able to
locate, on its own, the default target that has been expressly defined
for this purpose.

If you have attempted the above in the most direct way possible, you
have likely been met, in return, with something along these lines:

```
make: *** No targets specified and no makefile found.  Stop.
```

This is normal. In fact, it's intended. The aforementioned software
build automation utility exists, remains configured, and remains fully
functional. It has simply decided, for reasons that explain themselves
throughout the rest of this document, not to present itself to you
under its usual name.

Any resemblance between the above and the word Torturette is purely
linguistic coincidence.

---

## 8. Frequently asked questions

**What if I get stuck on an exercise?**
That is, in fact, the entire point of an exam.

**Can I use `evaluate` over and over without stopping?**
Technically, yes. Philosophically, the program would prefer you
reflect a little between attempts. It has its ways of insisting on
that.

**Why does the wait message say 30 seconds is "expected"?**
Because someone, at some point, decided that uncertainty is part of
the educational experience.

**What exactly is Torturette?**
A code name. Nothing more. Certainly not something you'd type into a
terminal, and any resemblance to something you actually could type
into a terminal is, as already stated, a coincidence.

**Where are the answers?**
Good question. That's one we're definitely not answering here.

**I don't understand anything this document says. What do I do?**
Read the manual.

**This document IS the manual.**
Then you already know what to do: read it. Again, if necessary.

**Does this document get longer the more you read it, or is that just
me?**
Both things can be true at once.

---

## 9. Final note

If you've made it this far looking for the exact command and still
haven't found it, congratulations: you have just completed, without
realizing it, the first exercise of the exam.

---

## Appendix I — On the difficulties of translation (non-operational)

This appendix exists because of a recurring complaint: that certain
terms in this document — Torturette among them — are difficult to
interpret correctly without outside help.

We regret to inform you that this project does not ship with a small
yellow fish that, once inserted into the examinee's ear, instantly and
automatically translates any confusing term into their native tongue.
Had it shipped with one, this appendix would not be necessary, and
neither, probably, would several of the preceding sections.

In the absence of such a fish, the examinee will have to make do with
their own powers of interpretation: the very same ones they've been
relying on so far, and with an identical rate of success.

You are nonetheless reminded that reading this document aloud to a
third party may produce an effect comparable to that of a certain
extraterrestrial poetry widely regarded as the third worst in the known
universe. Discretion is advised, and perhaps earplugs for whoever is
listening.

Of the entire document, this appendix contributes the least new
information, which, all things considered, is really saying something.

---

## Appendix II — Errata

Where this document mentions a Section 10, there isn't one. Where it
mentions a revision history, there isn't one of those either. Both
once existed and were removed for reasons no longer recorded anywhere,
which, at this point, should surprise no one.

Any other numerical inconsistency the reader may have noticed between
sections is considered, for all intents and purposes, part of the
design.

---

## Colophon

If this document had to be summarized in a single sentence, that
sentence would not be in this section, but hidden somewhere among the
earlier ones, camouflaged between others that say more or less the
same thing in different words.

Thank you for reading this far. Torturette, whatever it is, appreciates
it just the same.

And if, after all this, someone asks you how to start it, you already
know how to answer: tell them to read the manual.
