import pandas as pd


def load_data():

    gossip_fake = pd.read_csv("dataset/gossipcop_fake.csv")
    gossip_real = pd.read_csv("dataset/gossipcop_real.csv")

    politifact_fake = pd.read_csv("dataset/politifact_fake.csv")
    politifact_real = pd.read_csv("dataset/politifact_real.csv")

    gossip_fake["label"] = 0
    politifact_fake["label"] = 0

    gossip_real["label"] = 1
    politifact_real["label"] = 1

    df = pd.concat(
        [
            gossip_fake,
            gossip_real,
            politifact_fake,
            politifact_real
        ],
        ignore_index=True
    )

    return df


if __name__ == "__main__":

    df = load_data()

    df = df.dropna(subset=["title"])

    df.to_csv("dataset/final_dataset.csv", index=False)

    print("Dataset Shape:")
    print(df.shape)

    print("\nLabel Distribution:")
    print(df["label"].value_counts())

    print("\nColumns:")
    print(df.columns)

    print("\nDataset saved successfully!")