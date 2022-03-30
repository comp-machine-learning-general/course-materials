import numpy as np
import pandas as pd


def gini_index(data_pd: pd.DataFrame, class_var: str) -> float:
    """
    Given the observations of a binary class and the name of the binary class column
    calculate the gini index
    """
    # count classes 0 and 1
    count_A = np.sum(data_pd[class_var] == 0)
    count_B = np.sum(data_pd[class_var])

    # get the total observations
    n = count_A + count_B

    # If n is 0 then we return the lowest possible gini impurity
    if n == 0:
        return 0.0

    # Getting the probability to see each of the classes
    p1 = count_A / n
    p2 = count_B / n

    # Calculating gini
    gini = 1 - (p1 ** 2 + p2 ** 2)

    # Returning the gini impurity
    return gini


def info_gain(data_pd: pd.DataFrame, class_var: str, feature: str) -> float:
    """
    Calculates how much info we gain from a split compared to info at the current node
    """
    # compute the base gini impurity (at the current node)
    gini_base = gini_index(data_pd, class_var)

    # split on the feature
    node_left, node_right = split_bool(data_pd, feature)

    # count datapoints in each split and the whole dataset
    n_left = node_left.shape[0]
    n_right = node_left.shape[0]
    n = n_left + n_right

    # get left and right gini index
    gini_left = gini_index(node_left, class_var)
    gini_right = gini_index(node_right, class_var)

    # calculate weight for each node
    # according to proportion of data it contains from parent node
    w_left = n_left / n
    w_right = n_right / n

    # calculated weighted gini index
    w_gini = w_left * gini_left + w_right * gini_right

    # calculate the gain of this split
    gini_gain = gini_base - w_gini

    # return the best feature
    return gini_gain


## split on a boolean/binary variable
## should look very similar to your code in the block above
def split_bool(data_pd, column_name):
    """Returns two pandas dataframes:
    one where the specified variable is true,
    and the other where the specified variable is false"""
    node_left = data_pd[data_pd[column_name]]
    node_right = data_pd[~data_pd[column_name]]

    return node_left, node_right


def best_split(data_pd: pd.DataFrame, class_var: str, exclude_features: list = []) -> float:
    """
    Returns the name of the best feature to split on at this node.
    If the current node contains the most info (all splits lose information), return None.
    """
    # compute the base gini index (at the current node)
    gini_base = gini_index(data_pd, class_var)

    # initialize max_gain and best_feature
    max_gain = 0
    best_feature = None

    # create list of features of data_pd not including class_var
    features = data_pd.columns[:-1]

    # will be useful later - can skip for now
    # remove features we're excluding
    # (already made decision on this feature)
    features = [f for f in features if f not in exclude_features]

    # test a split on each feature
    for feature in features:
        info = info_gain(data_pd, class_var, feature)

        # check whether this is the greatest gain we've seen so far
        # and thus the best split we've seen so far
        if info > max_gain:
            best_feature = feature
            max_gain = info

    # return the best feature
    return best_feature


## build a decision tree from a node of data
def build_decision_tree(node_data: pd.DataFrame, class_var: str, depth: int = 0, exclude_features: list = []) -> None:
    # 0. stop at the base case
    max_depth = 2
    if depth >= max_depth:
        return

    # 1. determine which decision gives us the most information
    best_feature = best_split(node_data, class_var, exclude_features)
    print(f"{'>' * (depth + 1)}Splitting {node_data.shape[0]} data points on {best_feature}")

    # 2a. if best_feature == None, don't split further
    if best_feature == None:
        print(f"{'>' * (depth + 1)}No best next split.")
        return

    # 2b. else, make the split according to the best decision
    else:
        data_left, data_right = split_bool(node_data, best_feature)
        print(
            f"{'>' * (depth + 1)}Produces {data_left.shape[0]} True data points and {data_right.shape[0]} False data points")

        # and exclude this feature at future levels of the tree
        exclude_features.append(best_feature)

    # 3. continue recursively on each of the resulting two nodes
    build_decision_tree(data_left, class_var, depth + 1, exclude_features)
    build_decision_tree(data_right, class_var, depth + 1, exclude_features)
    return