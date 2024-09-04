from app.crud import insert_memory_info, get_last_n_records


def test_insert_and_retrieve_memory_info():
    insert_memory_info(8192, 2048, 6144)
    records = get_last_n_records(1)
    assert len(records) == 1
    assert records[0][2] == 8192
    assert records[0][3] == 2048
    assert records[0][4] == 6144
