import sys, os
cwd = os.getcwd()
sys.path.append(cwd)

from tool_provider import ToolProvider
from tool_consumer import ToolConsumer

def create_params_tp():
    '''
    Creates a set of launch parameters for a ToolConsumer.
    '''
    return {
          "lti_message_type": "basic-lti-launch-request",
          "lti_version": "LTI-1p0",
          "resource_link_id": "c28ddcf1b2b13c52757aed1fe9b2eb0a4e2710a3",
          "lis_result_sourcedid": "261-154-728-17-784",
          "lis_outcome_service_url": "http://localhost/lis_grade_passback",
          "launch_presentation_return_url": "http://example.com/lti_return",
          "custom_param1": "custom1",
          "custom_param2": "custom2",
          "ext_lti_message_type": "extension-lti-launch",
          "roles": "Learner,Instructor,Observer"
    }

def create_test_tp():
    '''
    Returns a new ToolProvider.
    '''
    return ToolProvider('hi', 'oi', create_params_tp())

def create_params_tc():
    '''
    Creates a set of launch parameters for a ToolConsumer.
    '''
    return {
            'resource_link_id': '120988f929-274612',
            'user_id': '292832126',
            'roles': 'Instructor',
            'lis_person_name_full': 'Jane Q. Public',
            'lis_person_contact_email_primary': 'user@school.edu',
            'context_id': '456434513',
            'context_title': 'Design of Personal Environments',
            'context_label': 'SI182',
            'lti_version': 'LTI-1p0',
            'lti_message_type': 'basic-lti-launch-request',
            'tool_consumer_instance_guid': 'lmsng.school.edu',
            'tool_consumer_instance_description': 'University of School (LMSng)',
    }

def create_test_tc():
    '''
    Returns a new ToolConsumer.
    '''
    tc = ToolConsumer.new('12345', 'secret', create_params_tc())
    tc.launch_url = 'http://dr-chuck.com/ims/php-simple/tool.php'
    tc.timestamp = '1251600739'
    tc.nonce = 'c8350c0e47782d16d2fa48b2090c1d8f'
    tc.set_non_spec_param('lis_person_sourced_id', 'school.edu:user')
    tc.set_non_spec_param('basiclti_submit', 'Launch Endpoint with BasicLTI Data')

    return tc
