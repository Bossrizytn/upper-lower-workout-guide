# Local Exercise GIFs

These files are the locally hosted workout GIFs used by `index.html`.

Why they are local:
- On July 1, 2026, the previously hotlinked `static.exercisedb.dev` GIF URLs started returning `401/403`, which made the live site fall back to the older SVG motions.
- Keeping the GIFs inside this repo makes the GitHub Pages build independent from third-party hotlink rules.

Source and mapping:
- Original exercise metadata came from the free ExerciseDB V1 ecosystem.
- The local mirror files were recovered from the public backup repo `omercotkd/exercises-gifs`.
- Mapping from ExerciseDB `media_id` to backup asset ids was checked against `hasaneyldrm/exercises-dataset`.

Guardrail:
- Do not switch `index.html` back to third-party GIF URLs.
- Run `python3 scripts/validate_workout_gifs.py` after any workout page asset change.
