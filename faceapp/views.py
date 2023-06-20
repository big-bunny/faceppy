from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .scripts.facial import detect_faces

def recognize_faces(request):
    if request.method == 'POST':
        video_file = request.FILES.get('media')
        if video_file is None:
            return JsonResponse({'error': 'No video file was provided.'}, status=400)

        # Save the uploaded video file to a temporary location
        video_path = '/tmp/uploaded_video.mp4'  # Temporary path to save the video file
        with open(video_path, 'wb') as f:
            for chunk in video_file.chunks():
                f.write(chunk)

        # Call the detect_faces function from your script
        detect_faces(video_path)

        # Redirect to the Gallery page
        return redirect('Gallery')
    elif request.method == 'GET':
        # Return a simple response for the GET request
        return HttpResponse("Server is running.")  # You can customize the response message
    else:
        # Return a response indicating that the method is not allowed
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

def gallery_view(request):
    # Add your logic to generate the gallery page
    return render(request, 'Gallery.vue')
