from flask import render_template, request
from app import db
from app.errors import bp
from app.api.errors import error_response as api_error_response


def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']

@bp.app_errorhandler(400)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(400)
    return render_template('errors/400.html',title="Bad Request"), 400

@bp.app_errorhandler(404)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(404)
    return render_template('errors/404.html',title="Not Found"), 404


@bp.app_errorhandler(500)
def internal_error(error):
    if wants_json_response():
        return api_error_response(500)
    return render_template('errors/500.html',title="Internal Server Error"), 500

@bp.app_errorhandler(429)
def too_many_requests(error):
    if wants_json_response():
        return api_error_response(429)
    return render_template('errors/429.html',title="Too Many Requests"), 429
