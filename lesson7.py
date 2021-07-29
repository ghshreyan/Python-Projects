import boto3


s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

cw = boto3.client('cloudwatch')


# buckets = s3.buckets.all()

# for b in buckets:
#     print(b)


# first_bucket = list(buckets)[0]


# s3_resource.upload_file('lesson6.py', 'wr-apps-data-test', 'python_lessons/lesson6_v1.py')



# dictionary = {'a': 1, 'b': 2}
#
# print(dictionary.keys())
#
# print(dictionary.values())
#
# print(dictionary.items())
#
# for (key, value) in dictionary.items():
#     print(key)
#     print(value)

dashboards = cw.list_dashboards()

# for (key, value) in dashboards.items():
#     print(key)
#     print(value)


dashboard_entries = dashboards['DashboardEntries']

for entry in dashboard_entries:
    print(entry['DashboardName'], entry['LastModified'])
