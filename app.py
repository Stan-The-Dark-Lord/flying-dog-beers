 #-*- coding: utf-8 -*-
import json
import base64
import time
import random
import datetime
from datetime import datetime as dt
import requests
import dash_player
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True

def stylemarg (a):
	return {'margin-bottom': '20px','backgroundColor': a}
	
app.layout = html.Div([
    dash_player.DashPlayer(
        id='video-player',
		playing=True,
        url='/static/ezgifcom-gif-maker_2bmSsLcp_dxTU.mp4',
        controls=False
    ),
	html.Button(id='color',style={'margin-bottom': '20px','backgroundColor': 'green'} ),
	html.Div('What is the color?',id='question', style={'margin-bottom': '20px'}),
    html.Button('green', id='green',n_clicks_timestamp=0),
    html.Button('blue', id='blue',n_clicks_timestamp=0),
	html.Button('red', id='red',n_clicks_timestamp=0),
    html.Div(id='div-current-time', style={'margin-bottom': '20px'}),
	html.Div(id='timestamp', style={'margin-bottom': '20px'}),

    html.Div(id='div-method-output')
])

Colo ={
		1:'red',
		2:'blue',
		3:'green'
		}


Data=random.randrange(1, 3)

@app.callback(Output('div-current-time', 'children'),
              [Input('video-player', 'currentTime')])
def update_time(currentTime):
    return 'Current Time: {}'.format(currentTime)


@app.callback(Output('div-method-output', 'children'),
              [Input('video-player', 'secondsLoaded')],
              [State('video-player', 'duration')])
def update_methods(secondsLoaded, duration):
    return 'Second Loaded: {}, Duration: {}'.format(secondsLoaded, duration)



		
@app.callback([Output('video-player', 'seekTo'),Output('color', 'style'),Output('timestamp', 'children')],
              [Input('red', 'n_clicks_timestamp'),Input('blue', 'n_clicks_timestamp'),Input('green', 'n_clicks_timestamp')],
			  [State('color', 'style')])
def set_seekTo(red,blue,green,style):



	if red > green and red > blue and style['backgroundColor']=='red':
		return None,stylemarg(Colo[random.randrange(1, 3)]), 'tred {} tgreen {} tblue {}'.format(str(red),str(green),str(blue))
	elif green > red and green > blue and style['backgroundColor']=='green':
		return None,stylemarg(Colo[random.randrange(1, 3)]),'tred {} tgreen {} tblue {}'.format(str(red),str(green),str(blue))
	elif blue > green and blue > red and style['backgroundColor']=='blue':
		return None,stylemarg(Colo[random.randrange(1, 3)]),'tred {} tgreen {} tblue {}'.format(str(red),str(green),str(blue))
	else:
		return 0,stylemarg(style['backgroundColor']),'tred {} tgreen {} tblue {}'.format(str(red),str(green),str(blue))
		



if __name__ == '__main__':
    app.run_server(debug=True)
