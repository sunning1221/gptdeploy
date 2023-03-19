EXECUTOR_FILE_NAME = 'executor.py'
TEST_EXECUTOR_FILE_NAME = 'test_executor.py'
REQUIREMENTS_FILE_NAME = 'requirements.txt'
DOCKER_FILE_NAME = 'Dockerfile'
CLIENT_FILE_NAME = 'client.py'

EXECUTOR_FILE_TAG = 'executor'
TEST_EXECUTOR_FILE_TAG = 'test_executor'
REQUIREMENTS_FILE_TAG = 'requirements'
DOCKER_FILE_TAG = 'dockerfile'
CLIENT_FILE_TAG = 'client'

TAG_TO_FILE_NAME = {
    EXECUTOR_FILE_TAG: EXECUTOR_FILE_NAME,
    TEST_EXECUTOR_FILE_TAG: TEST_EXECUTOR_FILE_NAME,
    REQUIREMENTS_FILE_TAG: REQUIREMENTS_FILE_NAME,
    DOCKER_FILE_TAG: DOCKER_FILE_NAME,
    CLIENT_FILE_TAG: CLIENT_FILE_NAME
}

EXECUTOR_FOLDER = 'executor'
FLOW_URL_PLACEHOLDER = 'jcloud.jina.ai'