"""
Evaluation metrics for ASR model
"""

from jiwer import wer
import pandas as pd


def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculate Word Error Rate between reference and hypothesis
    
    Args:
        reference: Ground truth transcription
        hypothesis: Model prediction
        
    Returns:
        WER as float (0.0 = perfect, 1.0 = completely wrong)
    """
    return wer(reference, hypothesis)


def evaluate_predictions(df: pd.DataFrame, 
                        reference_col: str = 'Transcription',
                        hypothesis_col: str = 'Prediction') -> dict:
    """
    Evaluate predictions on a dataset
    
    Args:
        df: DataFrame with reference and hypothesis columns
        reference_col: Column name for ground truth
        hypothesis_col: Column name for predictions
        
    Returns:
        Dictionary with evaluation metrics
    """
    # Calculate WER for each sample
    df['wer'] = df.apply(
        lambda row: calculate_wer(row[reference_col], row[hypothesis_col]), 
        axis=1
    )
    
    results = {
        'mean_wer': df['wer'].mean(),
        'median_wer': df['wer'].median(),
        'std_wer': df['wer'].std(),
        'min_wer': df['wer'].min(),
        'max_wer': df['wer'].max(),
        'perfect_transcriptions': (df['wer'] == 0).sum(),
        'total_samples': len(df)
    }
    
    return results


if __name__ == "__main__":
    # Test
    ref = "hello world this is a test"
    hyp = "hello world this is test"  # Missing 'a'
    
    wer_score = calculate_wer(ref, hyp)
    print(f"WER: {wer_score:.3f}")
