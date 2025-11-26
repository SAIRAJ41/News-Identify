import pandas as pd

def preprocess_data(input_path, output_path):
    # Define column names
    col_names = [
        'id', 'json_id', 'label', 'statement', 'subject', 'speaker',
        'speaker_job', 'state_info', 'party', 'barely_true_counts',
        'false_counts', 'half_true_counts', 'mostly_true_counts',
        'pants_on_fire_counts', 'context', 'justification'
    ]

    # Read the tsv file
    df = pd.read_csv(input_path, sep='\t', header=None, names=col_names)

    # Select only the statement and label columns
    df = df[['statement', 'label']]

    # Define a mapping from the original labels to the new ones
    label_mapping = {
        'false': 'fake',
        'pants-fire': 'fake',
        'barely-true': 'fake',
        'half-true': 'neutral',
        'mostly-true': 'real',
        'true': 'real'
    }

    # Apply the mapping
    df['label'] = df['label'].map(label_mapping)

    # Drop rows with missing labels
    df.dropna(subset=['label'], inplace=True)

    # Save the preprocessed data
    df.to_csv(output_path, index=False)


if __name__ == '__main__':
    preprocess_data('LIAR-PLUS/dataset/tsv/train2.tsv', 'train.csv')
    preprocess_data('LIAR-PLUS/dataset/tsv/val2.tsv', 'val.csv')
    preprocess_data('LIAR-PLUS/dataset/tsv/test2.tsv', 'test.csv')
