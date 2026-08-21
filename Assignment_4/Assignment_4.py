import pandas as pd

roll_no = "1024170346"

fixed_entries = [
    {"question": "what is the annual fee",
     "answer": "The annual fee is Rs 500.",
     "keywords": "fee cost price charge",
     "category": "billing"},

    {"question": "how to reset password",
     "answer": "Go to Settings > Reset Password.",
     "keywords": "password reset login",
     "category": "account"},

    {"question": "what are your working hours",
     "answer": "We are open 9 AM to 5 PM.",
     "keywords": "hours timing open time",
     "category": "general"},

    {"question": "how can i pay the fee",
     "answer": "You can pay via UPI, card, or net banking.",
     "keywords": "pay payment upi fee",
     "category": "billing"}
]

personalized_entries = [
    {"question": "how do i update my registered mobile number",
     "answer": "Go to Account Settings and update your mobile number.",
     "keywords": "mobile number update",
     "category": "account"},

    {"question": "how can i check my billing amount",
     "answer": "You can check your billing amount in the billing section.",
     "keywords": "billing amount bill",
     "category": "billing"}
]

entries = fixed_entries + personalized_entries

df = pd.DataFrame(entries)

print("Q1:")
print(df)


def score_query(query, df):
    query_words = query.lower().split()
    results = []

    for i, row in df.iterrows():
        keywords = row["keywords"].lower().split()
        score = sum(word in keywords for word in query_words)

        if score > 0:
            results.append((score, i))

    results.sort(reverse=True)

    for score, i in results:
        print("Score:", score)
        print(df.loc[i])
        print()


print("\nQ2:")
score_query("fee payment", df)


def same_category(category_name, df):
    return df[df["category"] == category_name]


print("\nQ3:")
print(same_category("account", df))


print("\nQ4:")
index = 0

new_keyword = input("Enter a new keyword: ")

df.loc[index, "keywords"] = df.loc[index, "keywords"] + " " + new_keyword

df.to_csv(roll_no + "_faq_data.csv", index=False)

print(df)


print("\nQ5:")
print(df.groupby("category").size())


def score_query_tie(query, df):
    query_words = query.lower().split()
    scores = []

    for i, row in df.iterrows():
        keywords = row["keywords"].lower().split()
        score = sum(word in keywords for word in query_words)
        scores.append((score, i))

    highest = max(score for score, i in scores)

    if highest == 0:
        print("No match")
        return

    print("Highest score:", highest)

    for score, i in scores:
        if score == highest:
            print(df.loc[i])
            print()


print("\nQ6 - Tie:")
score_query_tie("fee", df)

print("\nQ6 - No Tie:")
score_query_tie("password", df)