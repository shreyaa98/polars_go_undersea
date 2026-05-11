import polars as pl
import string
from random import choice


def random_char_gen():
    while True:
        yield choice(string.ascii_lowercase + string.ascii_uppercase)


def translate_polar_to_pingu(word):
    chars = ""
    for a, b in zip(word, random_char_gen()):
        chars += choice([a.lower, a.upper])()
        chars += b
    prefix = choice(["plo", "pok", "pur", "prt", "puk"])
    postfix = 'prrr'
    return prefix + chars + postfix


message = "..."
words = [translate_polar_to_pingu(w) for w in message.split()]

df = pl.DataFrame({"text": [message]})

result = (
    df
    .select(pl.col("text").str.split(" ").alias("words"))
    .explode("words")
    .with_columns(
        pl.col("words").map_elements(translate_polar_to_pingu).alias("translated")
    )
)

print(result)
