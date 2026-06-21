# Exercise Animation Source Report

This report compares the current workout page against the free hosted ExerciseDB V1 catalog.

Scope:
- 28 program slots in the workout page
- 26 unique movements after removing repeated entries
- Goal: decide which movements can be replaced with free live GIFs, which are only partial matches, and which should stay on the current SVG animations

Important caveat:
- ExerciseDB free GIFs are technically easy to hotlink from `static.exercisedb.dev`, but the broader ExerciseDB ecosystem is controlled by its own terms and availability.
- For a quick prototype this is workable.
- For a long-lived public site, relying entirely on third-party hosted GIF URLs is still a product risk.

## Summary

- Safe to replace now: 22 unique movements
- Use only if you accept a nearby variation: 4 unique movements
- Of those 4 partial matches, 2 are still better left on the current SVG
- Repeated slots can reuse the same asset:
  - `Machine Chest Press`
  - `Neutral-Grip Lat Pulldown`

## Replace Now

| Current move | ExerciseDB free match | Why it works | GIF |
|---|---|---|---|
| Machine Chest Press | `lever chest press` | Same machine chest press pattern; good visual substitute | `https://static.exercisedb.dev/media/DOoWcnA.gif` |
| Neutral-Grip Lat Pulldown | `twin handle parallel grip lat pulldown` | Very close grip and pull path | `https://static.exercisedb.dev/media/rkg41Fb.gif` |
| Chest-Supported Dumbbell Row | `dumbbell incline row` | Chest-supported bench row visual is close enough | `https://static.exercisedb.dev/media/7vG5o25.gif` |
| Seated Dumbbell Shoulder Press | `dumbbell seated shoulder press` | Direct match | `https://static.exercisedb.dev/media/znQUdHY.gif` |
| Pec Deck | `lever seated fly` | Same pec fly machine family | `https://static.exercisedb.dev/media/v3xmPAR.gif` |
| Dumbbell Lateral Raise | `dumbbell lateral raise` | Direct match | `https://static.exercisedb.dev/media/DsgkuIt.gif` |
| Incline Dumbbell Curl | `dumbbell incline curl` | Direct match | `https://static.exercisedb.dev/media/ae9UoXQ.gif` |
| Seated Dumbbell Overhead Triceps Extension | `dumbbell seated triceps extension` | Very close seated overhead triceps pattern | `https://static.exercisedb.dev/media/kont8Ut.gif` |
| Leg Press | `sled 45° leg press (side pov)` | Close enough for gym-floor use; same lower-body press pattern | `https://static.exercisedb.dev/media/2Qh2J1e.gif` |
| Dumbbell Romanian Deadlift | `dumbbell romanian deadlift` | Direct match | `https://static.exercisedb.dev/media/rR0LJzx.gif` |
| Seated Leg Curl | `lever seated leg curl` | Direct match in machine family | `https://static.exercisedb.dev/media/Zg3XY7P.gif` |
| Leg Extension | `lever leg extension` | Direct match in machine family | `https://static.exercisedb.dev/media/my33uHU.gif` |
| Standing Calf Raise Machine | `lever standing calf raise` | Direct match in machine family | `https://static.exercisedb.dev/media/ykUOVze.gif` |
| Incline Dumbbell Press | `dumbbell incline bench press` | Direct match | `https://static.exercisedb.dev/media/ns0SIbU.gif` |
| Seated Row Machine | `lever seated row` | Direct match in machine family | `https://static.exercisedb.dev/media/7I6LNUG.gif` |
| Machine Shoulder Press | `lever shoulder press` | Direct match in machine family | `https://static.exercisedb.dev/media/67n3r98.gif` |
| Reverse Pec Deck | `lever seated reverse fly` | Same reverse-fly machine pattern | `https://static.exercisedb.dev/media/myfUsKf.gif` |
| Dumbbell Hammer Curl | `dumbbell hammer curl` | Direct match | `https://static.exercisedb.dev/media/slDvUAU.gif` |
| Machine Dip | `lever seated dip` | Good machine triceps-dip substitute | `https://static.exercisedb.dev/media/BRImeP8.gif` |
| Goblet Squat | `dumbbell goblet squat` | Direct match | `https://static.exercisedb.dev/media/yn8yg1r.gif` |
| One-Arm Dumbbell Row | `dumbbell one arm bent-over row` | Direct match | `https://static.exercisedb.dev/media/C0MA9bC.gif` |
| Machine Ab Crunch | `lever seated crunch (chest pad)` | Very close machine crunch pattern | `https://static.exercisedb.dev/media/ZnJHhMk.gif` |

## Use If You Accept A Nearby Variation

| Current move | ExerciseDB free match | Why it is only partial | GIF |
|---|---|---|---|
| Dumbbell Bulgarian Split Squat | `dumbbell single leg split squat` | Split squat is close, but rear-foot-elevated Bulgarian setup is not explicit | `https://static.exercisedb.dev/media/qx4fgX7.gif` |
| Wide-Grip Lat Pulldown | `cable wide grip rear pulldown behind neck` | It is wide-grip, but behind-neck makes it a different coaching choice | `https://static.exercisedb.dev/media/CmEr4pM.gif` |
| Hip Thrust Machine | `barbell glute bridge two legs on bench (male)` | Same glute-extension family, but not a hip thrust machine visual | `https://static.exercisedb.dev/media/qg2PGl6.gif` |
| Dumbbell Walking Lunge | `walking lunge` | The walking pattern is right, but the free match is bodyweight rather than dumbbell-loaded | `https://static.exercisedb.dev/media/IZVHb27.gif` |

## Keep Current SVG

These are the ones I would keep as the current custom SVG animations if the goal is a cleaner and more precise phone experience.

| Current move | Why keep SVG |
|---|---|
| Wide-Grip Lat Pulldown | The best free match is behind-neck, which is not the same technical cueing we want in the program |
| Hip Thrust Machine | Free catalog does not give a true machine hip thrust visual; the substitute looks like a different exercise to most users |

## Practical Recommendation

Best hybrid setup:
- Swap in ExerciseDB free GIFs for the `Replace Now` group
- Keep SVGs for `Wide-Grip Lat Pulldown` and `Hip Thrust Machine`
- Decide case-by-case for:
  - `Dumbbell Bulgarian Split Squat`
  - `Dumbbell Walking Lunge`

If we want the cleanest mobile result without paying for assets:
- Use a hybrid page with mostly free GIFs
- Preserve SVGs where the free catalog is visually misleading

If we want the cleanest final product overall:
- Use this report as the selection shortlist
- Replace the weak matches later with paid/licensed assets or custom animations

## Source Notes

- ExerciseDB GitHub repo: `https://github.com/ExerciseDB/exercisedb-api`
- ExerciseDB free hosted V1 docs: `https://docs.ascendapi.com/products/edb-v1/overview`
- ExerciseDB API reference intro: `https://docs.ascendapi.com/api-reference/introduction`
- ExerciseDB terms page reviewed: `https://edb-docs.up.railway.app/docs/api-terms-of-use`
- Muscle & Strength remains useful for exercise reading/reference, but not as an embed/scrape source for this site:
  - `https://www.muscleandstrength.com/exercises`
  - `https://www.muscleandstrength.com/terms.html`
