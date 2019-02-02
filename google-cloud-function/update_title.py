from google.cloud import storage

def update_title(request):
    
    """
    Updates title.html to reflect the title desired
    """
    request_json = request.get_json()
    if request.args and 'title' in request.args:
        with open("/tmp/tempfile", "w") as f:
            f.write(request.args.get('title'))
        resp = upload_blob("arcademachine", "/tmp/tempfile", "title.html")
        return resp
    else:
        return "Error"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.cache_control = "no-cache"
    blob.upload_from_filename(source_file_name, content_type="text/html")
    blob.make_public()
    resp = 'File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name)
    return resp
