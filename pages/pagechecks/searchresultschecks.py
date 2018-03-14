from pages.pageobjects.searchresults import results_filtered


def check_labels(expected_label):
    assert results_filtered(expected_label)
