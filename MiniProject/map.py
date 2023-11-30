from dash import Dash, dcc, html, Output, Input, callback
import plotly.express as px
import pandas as pd
app = Dash(__name__)
df = pd.read_csv("yearly_dataset.csv")

# Pivot the DataFrame for heatmap
heatmap_df = df.pivot_table(values='Count', index='region', columns='Influenza_Category', aggfunc='sum', fill_value=0)

# Plot the heatmap using Plotly Express
fig = px.imshow(heatmap_df, labels=dict(x="Influenza_Category", y="region", color="Count"),
                x=heatmap_df.columns, y=heatmap_df.index, color_continuous_scale='blues')

fig.update_layout(title='Influenza Cases by Region and Category')


app.layout = html.Div([
    html.H4('Inluenza Analysis'),
    dcc.Graph(id='hmap', figure=fig), 
    # Dropdown for selecting different options
    dcc.Dropdown(
        id='dropdown-option',
        options=[
            {'label': 'select the year 09', 'value': 9},
            {'label': 'select the year 10', 'value': 10},
            {'label': 'select the year 11', 'value': 11},
            {'label': 'select the year 12', 'value': 12},
            {'label': 'select the year 13', 'value': 13},
            {'label': 'select the year 14', 'value': 14},
            {'label': 'select the year 15', 'value': 15},
            {'label': 'select the year 16', 'value': 16},
            {'label': 'select the year 17', 'value': 17},
            {'label': 'select the year 18', 'value': 17},
            {'label': 'select the year 19', 'value': 19},
            {'label': 'select the year 20', 'value': 20},


        ],
    ),
  dcc.Graph(id='type_data'),  # Initial empty graph
])
#type yearly graphs graphs
@callback(
    Output('type_data', 'figure'),
    Input('dropdown-option', 'value')
)
def plotYrlyGraph(selected_option):
    if selected_option == 9:
        type_df = pd.read_csv("./type_year_data/09.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 10:
        type_df = pd.read_csv("./type_year_data/10.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 11:
        type_df = pd.read_csv("./type_year_data/11.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 12:
        type_df = pd.read_csv("./type_year_data/12.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 13:
        type_df = pd.read_csv("./type_year_data/13.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 14:
        type_df = pd.read_csv("./type_year_data/14.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 15:
        type_df = pd.read_csv("./type_year_data/15.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 16:
        type_df = pd.read_csv("./type_year_data/16.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 17:
        type_df = pd.read_csv("./type_year_data/17.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 18:
        type_df = pd.read_csv("./type_year_data/18.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    elif selected_option == 19:
        type_df = pd.read_csv("./type_year_data/19.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    else:
        type_df = pd.read_csv("./type_year_data/20.csv", names=['type', 'count'])
        br_plt= px.bar(type_df, x='type', y='count', color='count',
             labels={'Count': 'Influenza Cases Count'},
             title='Influenza Cases by Category')
    return br_plt

if __name__=='__main__':
    app.run(debug=True)