<%page args="form, action_url"/>

<div class="hide form" id="${form.id}">
    <form action="${action_url}" method="POST">
        ${form.obj_id}
    </form>
</div>
