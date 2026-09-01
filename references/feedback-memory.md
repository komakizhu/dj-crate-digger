# Feedback and private taste memory

Load this resource when a user comments on recommendations or when the report reaches its optional feedback action. Accept ordinary language, pasted rows, links, screenshots, and statements about liking, disliking, using, not using, or having already played a track. The user never needs to learn internal feedback labels.

## Interpretation

Translate each message into the most specific applicable target first: recording/title variant, then artist, then style or scene. Apply weak upward generalization rather than letting one track change an entire genre profile. Keep taste and scene utility separate: “I like it but not for this wedding” updates taste positively and wedding utility negatively, not both in the same direction.

Use weighted Beta-Bernoulli evidence with time decay. Example weights are `liked` +0.5 to taste, `would_use` +1 to scene utility, `actually_used` +2 to scene utility, `disliked` +1 negative to taste, and `wrong_scene` only to scene utility. Long-term memory contributes at most 10% of recommendation weight; current request, verified evidence, scene, and explicit constraints dominate.

If interpretation confidence is low, do not update even the current profile. Keep the raw message pending for the next summary correction. A high-confidence single message can affect the current session, but it is not by itself stable long-term preference evidence.

## Storage and confirmation

Store two layers locally and privately: immutable feedback events for correction/recalculation, and a rebuildable profile summary for recommendation. The current session applies feedback automatically. At the end of a feedback round, present one concise taste-change summary—not one prompt per track—and ask for explicit confirmation before saving it to the long-term profile. A negative or unclear response saves nothing; an unclear confirmation gets one clarification only. Do not upload personal feedback or implement anonymous collaboration.
