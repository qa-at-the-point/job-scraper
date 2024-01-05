from jobs import ai


def test_convert_clean_response():
    response = """
        [
            {
                "title": "QA Engineer, Manual Tester",
                "company": "i2e Consulting"
            },
            {
                "title": "Junior Manual tester",
                "company": "Technimates LLC"
            }
        ]
    """
    output = ai.convert_relevant_jobs_to_list(response)

    assert isinstance(output, list)
    assert len(output) == 2
    assert output[0]["title"] == "QA Engineer, Manual Tester"
    assert output[0]["company"] == "i2e Consulting"


def test_convert_backtick_response():
    response = """
    ```
        [
            {
                "title": "QA Engineer, Manual Tester",
                "company": "i2e Consulting"
            },
            {
                "title": "Junior Manual tester",
                "company": "Technimates LLC"
            }
        ]
    ```
    """
    output = ai.convert_relevant_jobs_to_list(response)

    assert isinstance(output, list)
    assert len(output) == 2
    assert output[0]["title"] == "QA Engineer, Manual Tester"
    assert output[0]["company"] == "i2e Consulting"


def test_convert_backtick_with_header_response():
    response = """
    ```json
        [
            {
                "title": "QA Engineer, Manual Tester",
                "company": "i2e Consulting"
            },
            {
                "title": "Junior Manual tester",
                "company": "Technimates LLC"
            }
        ]
    ```
    """
    output = ai.convert_relevant_jobs_to_list(response)

    assert isinstance(output, list)
    assert len(output) == 2
    assert output[0]["title"] == "QA Engineer, Manual Tester"
    assert output[0]["company"] == "i2e Consulting"


def test_convert_extra_wording_response():
    response = """
    Certainly! Here are the relevant jobs:

    ```json
        [
            {
                "title": "QA Engineer, Manual Tester",
                "company": "i2e Consulting"
            },
            {
                "title": "Junior Manual tester",
                "company": "Technimates LLC"
            }
        ]
    ```

    I hope this helps!
    """
    output = ai.convert_relevant_jobs_to_list(response)

    assert isinstance(output, list)
    assert len(output) == 2
    assert output[0]["title"] == "QA Engineer, Manual Tester"
    assert output[0]["company"] == "i2e Consulting"
