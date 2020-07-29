def test_myapp_case1(dbr_client):
    result = dbr_client.execute('/Test-AssertEquals-DataFrames')
    assert result.was_successful == True
