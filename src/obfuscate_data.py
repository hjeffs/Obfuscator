def obfuscate_data(dataframe, fields):
    print(dataframe, '<<< DATA (INPUT)')
    for field in fields:
        if field in dataframe.columns:
            dataframe[field] = '***' # Obfuscated value from brief
    # print(dataframe)
    return dataframe