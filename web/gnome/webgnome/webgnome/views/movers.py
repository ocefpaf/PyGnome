from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.renderers import render
from pyramid.view import view_config


from ..forms import (
    AddMoverForm,
    VariableWindMoverForm,
    ConstantWindMoverForm,
    MOVER_VARIABLE_WIND,
    MOVER_CONSTANT_WIND
)

from ..util import json_require_model, make_message


@view_config(route_name='edit_constant_wind_mover', renderer='gnome_json')
@json_require_model
def edit_constant_wind_mover(request, model):
    mover_id = request.matchdict['id']
    mover = model.get_mover(mover_id)
    opts = {'obj': mover} if mover else {}
    form = ConstantWindMoverForm(request.POST or None, **opts)

    if request.method == 'POST' and form.validate():
        if model.has_mover_with_id(mover_id):
            model.update_mover(mover_id, form.data)
            message = make_message(
                'success', 'Updated constant wind mover successfully.')
        else:
            mover_id = model.add_mover(form.data)
            message = make_message('warning',
                                    'The specified mover did not exist. Added '
                                    'a new constant wind mover to the model.')
        return {
            'id': mover_id,
            'message': message,
            'form_html': None
        }

    html = render('webgnome:templates/forms/constant_wind_mover.mak', {
        'form': form,
        'action_url': request.route_url(
            'edit_constant_wind_mover', id=mover_id)
    })

    return {'form_html': html}


@view_config(route_name='edit_variable_wind_mover', renderer='gnome_json')
@json_require_model
def edit_variable_wind_mover(request, model):
    mover_id = request.matchdict['id']
    mover = model.get_mover(mover_id)
    opts = {'obj': mover} if mover else {}
    form = VariableWindMoverForm(request.POST or None, **opts)

    if request.method == 'POST' and form.validate():
        if model.has_mover_with_id(mover_id):
            model.update_mover(mover_id, form.data)
            message = make_message(
                'success', 'Updated variable wind mover successfully.')
        else:
            mover_id = model.add_mover(form.data)
            message = make_message('warning',
                                    'The specified mover did not exist. Added '
                                    'a new variable wind mover to the model.')
        return {
            'id': mover_id,
            'message': message,
            'form_html': None
        }

    html = render('webgnome:templates/forms/variable_wind_mover.mak', {
        'form': form,
        'action_url': request.route_url('edit_variable_wind_mover',
                                        id=mover_id)
    })

    return {'form_html': html}


@view_config(route_name='add_constant_wind_mover', renderer='gnome_json')
@json_require_model
def add_constant_wind_mover(request, model):
    form = ConstantWindMoverForm(request.POST)

    if request.method == 'POST' and form.validate():
        mover = None
        # TODO: Create wind mover here.
        return {
            'id': model.add_mover(mover),
            'type': 'mover',
            'form_html': None
        }

    html = render('webgnome:templates/forms/constant_wind_mover.mak', {
        'form': form,
        'action_url': request.route_url('add_constant_wind_mover')
    })

    return {'form_html': html}


@view_config(route_name='add_variable_wind_mover', renderer='gnome_json')
@json_require_model
def add_variable_wind_mover(request, model):
    form = VariableWindMoverForm(request.POST)

    if request.method == 'POST' and form.validate():
        return {
            'id': model.add_mover(form.data),
            'type': 'mover',
            'form_html': None
        }

    context = {
        'form': form,
        'action_url': request.route_url('add_variable_wind_mover')
    }

    return {
        'form_html': render(
            'webgnome:templates/forms/variable_wind_mover.mak', context)
    }


@view_config(route_name='delete_mover', renderer='gnome_json', request_method='POST')
@json_require_model
def delete_mover(request, model):
    mover_id = request.POST.get('mover_id', None)

    if mover_id is None or model.has_mover_with_id(mover_id) is False:
        raise HTTPNotFound

    model.delete_mover(mover_id)

    return {
        'success': True
    }
