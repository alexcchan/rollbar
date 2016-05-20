"""
API MAPPING FOR Rollbar API V1
"""

mapping_table = {

    'content_type': 'application/x-www-form-urlencoded',
    'path_prefix': '/api/1',

    'get_deploy': {
        'method': 'GET',
        'path': '/deploy/{{deploy_id}}',
    },

    'list_deploys': {
        'method': 'GET',
        'path': '/deploys/',
        'valid_params': ['page'],
    },

    'get_invite': {
        'method': 'GET',
        'path': '/item/{{invite_id}}',
    },

    'list_team_invites': {
        'method': 'GET',
        'path': '/team/{{team_id}}/invites',
        'valid_params': ['page'],
    },

    'get_item': {
        'method': 'GET',
        'path': '/item/{{item_id}}',
    },

    'list_items': {
        'method': 'GET',
        'path': '/items/',
        'valid_params': ['page'],
    },

    'get_item_by_counter': {
        'method': 'GET',
        'path': '/item_by_counter/{{counter_id}}',
        'status': 301,
    },

    'get_occurrence': {
        'method': 'GET',
        'path': '/instance/{{occurrence_id}}',
    },

    'list_occurrences': {
        'method': 'GET',
        'path': '/instances/',
        'valid_params': ['page'],
    },

    'list_item_occurrences': {
        'method': 'GET',
        'path': '/item/{{item_id}}/instances/',
        'valid_params': ['page'],
    },

    'get_project': {
        'method': 'GET',
        'path': '/project/{{project_id}}',
    },

    'list_projects': {
        'method': 'GET',
        'path': '/projects',
        'valid_params': ['page'],
    },

    'list_project_access_tokens': {
        'method': 'GET',
        'path': '/project/{{project_id}}/access_tokens',
        'valid_params': ['page'],
    },

    'get_rql_job': {
        'method': 'GET',
        'path': '/rql/job/{{job_id}}',
    },

    'get_rql_job_result': {
        'method': 'GET',
        'path': '/rql/job/{{job_id}}/result',
    },

    'list_rql_jobs': {
        'method': 'GET',
        'path': '/rql/jobs',
        'valid_params': ['page'],
    },

    'get_team': {
        'method': 'GET',
        'path': '/team/{{team_id}}',
    },

    'list_teams': {
        'method': 'GET',
        'path': '/teams',
        'valid_params': ['page'],
    },

    'get_team_project': {
        'method': 'GET',
        'path': '/team/{{team_id}}/project/{{project_id}}',
    },

    'list_team_projects': {
        'method': 'GET',
        'path': '/team/{{team_id}}/projects',
        'valid_params': ['page'],
    },

    'get_team_user': {
        'method': 'GET',
        'path': '/team/{{team_id}}/user/{{user_id}}',
    },

    'list_team_users': {
        'method': 'GET',
        'path': '/team/{{team_id}}/users',
        'valid_params': ['page'],
    },

    'get_user': {
        'method': 'GET',
        'path': '/user/{{user_id}}',
    },

    'report_top_recent_active_items': {
        'method': 'GET',
        'path': '/reports/top_active_items',
    },

    'report_occurrence_counts': {
        'method': 'GET',
        'path': '/reports/occurrence_counts',
    },

    'report_activated_counts': {
        'method': 'GET',
        'path': '/reports/activated_counts',
    },


}
