from os.path import dirname, join, realpath, basename
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from secret import COGNITIVE_SERVICE_KEY, COGNITIVE_SERVICE_ENDPOINT


def get_face_emotion_information(input_file_path):
    """
    This function takes full file path to the image (type: string) and sends to Azure API. If the face is detected, then the emotion analysis
    will be returned.
    Note: .png, .jpg, or .gif file type only. Allowed file size is from 1KB to 6MB
    """
    # # The resource key for the MistyFaceEmotionDetection Resource on Azure
    # The variable is for the ACS API, created with the cognitive services resource
    COGNITIVE_SERVICE_KEY = "1837b9d29e0b4a22843d103a7ca8b3c9"
    COGNITIVE_SERVICE_ENDPOINT = "https://westus2.api.cognitive.microsoft.com/"

    # Authenticating the Client
    face_client = FaceClient(COGNITIVE_SERVICE_ENDPOINT, CognitiveServicesCredentials(COGNITIVE_SERVICE_KEY))

    # Creating an image stream given an input image file.
    # returns only the number of faces found, up to 100
    with open(input_file_path, "rb") as faces:
        detected_faces = face_client.face.detect_with_stream(faces, return_face_attributes = FaceAttributeType.emotion)

    # Variables used later on.
    image_name = basename(input_file_path)
    returning_dictionary = {}
    count = 0

    # Case: There are no faces detected in the image.
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(input_file_path))

    # Creating a unique dictionary object for each face detected from the given file and adding it
    # to the returning_dictionary dictionary.

    for face in detected_faces:
        Dict = {}
        Dict["anger"] = face.face_attributes.emotion.anger
        Dict["contempt"] = face.face_attributes.emotion.contempt
        Dict["disgust"] = face.face_attributes.emotion.disgust
        Dict["fear"] = face.face_attributes.emotion.fear
        Dict["happiness"] = face.face_attributes.emotion.happiness
        Dict["neutral"] = face.face_attributes.emotion.neutral
        Dict["sadness"] = face.face_attributes.emotion.sadness
        Dict["surprise"] = face.face_attributes.emotion.surprise
        returning_dictionary["face" + str(count)] = Dict
        count += 1

    d = returning_dictionary.get('face' + str(0))
    # taking list of car values in v
    v = list(d.values())
    # taking list of car keys in v
    k = list(d.keys())
    print(k[v.index(max(v))])
    emotion = k[v.index(max(v))]

    return emotion
