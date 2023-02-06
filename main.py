def main():
    fp = 'C:\\Users\\Dr Blue\\research\\data\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
    import pandas as pd
    df = pd.read_json(fp, lines=True, chunksize=1000)
    print(df.shape)
    print(df[df['order_item_order_id']==2])

if __name__ == "__main__":
    main()