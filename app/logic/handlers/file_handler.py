# logic/handlers/file_handler.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from logic.core.encryption import encrypt_file, generate_key
from logic.core.file_store_model import create_encrypted_file_local, create_encrypted_file_aws_s3
from configs.config import get_config

@csrf_exempt
def upload_file(request):
    #print(f"Headers: {request.headers}")
    #print(f"Content Type: {request.content_type}")
    #print(f"Files: {request.FILES}")

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        file_content = uploaded_file.read()
        key = generate_key()
        encrypted_content = encrypt_file(file_content, key)

        storage_option = get_config('STORAGE_OPTION', 'filesystem')

        if storage_option == 's3':
            create_encrypted_file_aws_s3(file_name, encrypted_content)
        else:
            create_encrypted_file_local(file_name, encrypted_content)

        return JsonResponse({'message': 'File uploaded successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)
