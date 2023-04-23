{% extends "layout.html" %}

{% block title %}L.E.C.I Internship Platform{% endblock %}

{% block page %}L.E.C.I Internship Platform{% endblock %}


{% block content %}
<div class="content fill-space">
  <img class="grow-2" src="https://test.ishmaeljup.repl.co/image.png">
  <div class="subcontent center-vertical">
    <h4 class="center">Login</h4>
    <form id="loginForm" method="POST" action="/login" style="padding:1em">

      <div class="row">
        <div class="input-field col s12">
          <input placeholder="Placeholder" id="username" name="username" type="text" class="validate">
          <label for="username">Username</label>
        </div>
      </div>
      <div class="row">
        <div class="input-field col s12">
          <input name="password" id="password" type="password" class="validate">
          <label for="password">Password</label>
        </div>
      </div>
      <div class="row justify-content">
        <div class="col s4 card-action">
          <input type="submit" class="blue text-white btn" value="Login">
        </div>

        <div class="col s8 card-action right-align">
          <a href="/signup">Don't have an account? Sign Up</a>
        </div>
      </div>

    </form>
  </div>

</div>
{% endblock %}
