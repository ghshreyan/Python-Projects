import boto3


s3 = boto3.resource('s3')



buckets = s3.buckets.all()
#
# for b in buckets:
#     print(b.name)



# a = list(buckets)[0]
#
# print(dir(a))

print(dir(list))
