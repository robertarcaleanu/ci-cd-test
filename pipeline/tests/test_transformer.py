from pipeline.src.transform import Transformer, balance_dataset
import pytest
import pandas as pd

# Sample fixture to create a mock DataFrame
@pytest.fixture
def df():
    return pd.DataFrame({
        'age': [25, 30, 35, 40],
        'job': ['admin', 'technician', 'admin', 'technician'],
        'marital': ['single', 'married', 'single', 'married'],
        'month': ['jan', 'feb', 'mar', 'apr'],
        'y': ['yes', 'no', 'yes', 'no'],
        'education': ['highschool', 'bachelor', 'highschool', 'bachelor'],
        'housing': ['yes', 'no', 'yes', 'no'],
        'loan': ['no', 'no', 'yes', 'yes'],
    })


# Fixture for Transformer instance
@pytest.fixture
def transformer():
    return Transformer()


# Test for Transformer class
def test_transform(transformer, df):
    # Define the expected output
    expected_df = pd.DataFrame({
        'month': [1, 2, 3, 4],  # Jan -> 1, Feb -> 2, Mar -> 3, Apr -> 4
        'education_bachelor': [0, 1, 0, 1],
        'education_highschool': [1, 0, 1, 0],
        'housing': [1, 0, 1, 0],
        'loan': [0, 0, 1, 1]
    })

    # Apply transformation
    transformed_df = transformer.transform(df.copy())
    
    # Test the result against the expected DataFrame
    pd.testing.assert_frame_equal(transformed_df, expected_df)


def test_map_binary_column_to_int(transformer):
    df = pd.DataFrame({
        'housing': ['yes', 'no', 'yes', 'no'],
        'loan': ['no', 'yes', 'yes', 'no']
    })
    
    expected_df = pd.DataFrame({
        'housing': [1, 0, 1, 0],
        'loan': [0, 1, 1, 0]
    })
    
    transformed_df = transformer._map_binary_column_to_int(df)
    
    # Test the result against the expected DataFrame
    pd.testing.assert_frame_equal(transformed_df, expected_df)


def test_map_month_to_int(transformer):
    df = pd.DataFrame({
        'month': ['jan', 'feb', 'mar', 'apr']
    })
    
    expected_df = pd.DataFrame({
        'month': [1, 2, 3, 4]
    })
    
    transformed_df = transformer._map_month_to_int(df)
    
    # Test the result against the expected DataFrame
    pd.testing.assert_frame_equal(transformed_df, expected_df)


def test_one_hot_encoding(transformer):
    df = pd.DataFrame({
        'education': ['highschool', 'bachelor', 'highschool', 'bachelor']
    })
    
    expected_df = pd.DataFrame({
        'education_bachelor': [0, 1, 0, 1],
        'education_highschool': [1, 0, 1, 0]
    })
    
    transformed_df = transformer._one_hot_encoding(df)
    
    # Test the result against the expected DataFrame
    pd.testing.assert_frame_equal(transformed_df, expected_df)


# Test for balance_dataset function
@pytest.fixture
def df_balance():
    return pd.DataFrame({
        'age': [25, 30, 35, 40, 45, 50],
        'job': ['admin', 'technician', 'admin', 'technician', 'admin', 'technician'],
        'y': ['yes', 'no', 'yes', 'no', 'yes', 'no']
    })


def test_balance_dataset(df_balance):
    # Define the expected balanced output
    expected_df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45, 50],
        'job': ['admin', 'technician', 'admin', 'technician', 'admin', 'technician'],
        'y': ['yes', 'no', 'yes', 'no', 'yes', 'no']
    })

    # Before balancing
    assert df_balance['y'].value_counts()['yes'] == 3
    assert df_balance['y'].value_counts()['no'] == 3
    
    # Balance the dataset
    balanced_df = balance_dataset(df_balance)

    # After balancing
    assert balanced_df['y'].value_counts()['yes'] == 3
    assert balanced_df['y'].value_counts()['no'] == 3

    # Check if the index was reset
    assert balanced_df.index.is_unique

    # Test the result against the expected DataFrame (order may vary)
    pd.testing.assert_frame_equal(balanced_df.sort_index(axis=1), expected_df.sort_index(axis=1))


def test_balance_with_unequal_classes():
    df_unequal = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'job': ['admin', 'technician', 'admin', 'technician', 'admin'],
        'y': ['yes', 'no', 'yes', 'no', 'yes']
    })
    
    # Define the expected balanced output
    expected_df = pd.DataFrame({
        'age': [25, 30, 35, 40],
        'job': ['admin', 'technician', 'admin', 'technician'],
        'y': ['yes', 'no', 'yes', 'no']
    })
    
    # Before balancing
    assert df_unequal['y'].value_counts()['yes'] == 3
    assert df_unequal['y'].value_counts()['no'] == 2
    
    # Balance the dataset
    balanced_df = balance_dataset(df_unequal)

    # After balancing
    assert balanced_df['y'].value_counts()['yes'] == 2
    assert balanced_df['y'].value_counts()['no'] == 2

    # Check if the index was reset
    assert balanced_df.index.is_unique

    # Test the result against the expected DataFrame (order may vary)
    pd.testing.assert_frame_equal(balanced_df.sort_index(axis=1), expected_df.sort_index(axis=1))
