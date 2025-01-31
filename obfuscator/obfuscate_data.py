def obfuscate_data(dataframe, fields):
    print(dataframe, '<<< DATA (INPUT) in obfuscate_data.py')
    for field in fields:
        if field in dataframe.columns:
            dataframe[field] = '***' # Obfuscated value from brief
    # print(dataframe)
    return dataframe