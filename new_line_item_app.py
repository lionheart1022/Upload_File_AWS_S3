import os
from aws import upload_file_to_s3

def create_item(line_item):
	
	item = None # map line_item to item as described in the doc
	
	upload_success = True
	failure_reason = ''
	
	# ad network upload code goes here (removed for privacy)

	# ad network upload is done
	
	if upload_success:
		line_item_id = '4986011' #test line item id returned from upload
	else:
		# set failure reason on line item and save, exit
		pass

    creative_file = item['Creative File']

    ext = os.path.basename(creative_file).rsplit('.')[-1]
    filename_template = (
        '{creative_prefix}JUMPTAP{line_item_id}{creative_postfix}'
        '.{creative_file_extension}'
    )
    filename = filename_template.format(
        creative_prefix=item['Creative Prefix'],
        line_item_id=line_item_id,
        creative_postfix=item['Creative Postfix'],
        creative_file_extension=ext
    )

    if upload_path:
        filename = os.path.join(upload_path, filename)
    uploaded_url = upload_file_to_s3(creative_file, filename)
