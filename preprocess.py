import re
import pandas as pd
def preprocess(data):
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}) - (.*?): (.*)'

    # Extract the message tuples
    messages = re.findall(pattern, data)

    # Create the DataFrame
    df = pd.DataFrame(messages, columns=["Date", "Time", "Sender", "Message"])

    # Optional: Combine date and time into datetime
    df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], dayfirst=False)

    # Reorder columns
    df = df[["Datetime", "Sender", "Message"]]
    df['year'] = df['Datetime'].dt.year
    df['month_num'] = df['Datetime'].dt.month
    df['month'] = df['Datetime'].dt.month_name()
    df['day']= df['Datetime'].dt.day
    df['day_name'] = df['Datetime'].dt.day_name()
    df['hour']= df['Datetime'].dt.hour
    df['minute']= df['Datetime'].dt.minute
    period = []
    for h in df[['day_name', 'hour']]['hour']:
        if h == 23:
            period.append(str(h)+'-'+str('00'))
        elif h == 0:
            period.append(str('00')+'-'+str(h+1))
        else:
            period.append(str(h)+'-'+str(h+1))
    df['period'] = period
    return df