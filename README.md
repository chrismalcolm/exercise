# Exercise Program

Simple exercise program.

Specify the exercises and exercise options in the `config.json` file. See the example below:

```json
{
    "exercise_time": 40,
    "cooldown_time": 20,
    "count": 15,
    "exercises": {
        "<category-1": [
            "<exercise-1>",
            "<exercise-2>",
            "<exercise-3>",
            "<exercise-4>"
        ],
        "<category-2": [
            "<exercise-5>"
        ],
        "<category-3": [
            "<exercise-6>",
            "<exercise-7>"
        ]
    }
}
```

`exercise_time` - duration of each exercise

`cooldown_time` - cooldown duration between exercises

`count` - number of exercises to be picked

`exercises` is a JSON object, with category names as the keys and list of exercises as the values. The Exercise Program will create a routine by randomly selecting exercises from each category. Unless it is impossible, exercises will be chosen such that consecutive exercises will **not** be from the same category.

Once `config.json` has been configured, run `python3 app.py` and the exercise program will start. The workout exercises and routine will be displayed in the CLI.

Upon review of the exrecises, you can start the workout. The Exercise Program will accounce exercise starts, halfway marks, exercise finishes, cooldown and completion.

Enjoy!
