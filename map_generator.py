
#Mapping Gentrification for Red Hook - Current Year
with urlopen('https://gist.githubusercontent.com/akash-y/eec842afd41ca3090ee402a235faeb37/raw/1e93801cd084e00c4b49a90582e7578689787354/test.geojson') as response:
    tracts = json.load(response)

gentrification_2018_df = pd.read_csv('https://gist.githubusercontent.com/akash-y/aa7e340b02ac6f8cc78b3f5698bb95b8/raw/87deac83e18a099ac02ca215e3af354c7581f4eb/redhook_predictions_2018.csv')



fig2 = px.choropleth_mapbox(gentrification_2018_df, geojson=tracts,locations = 'geo_id' ,featureidkey="properties.geo_id",color='prediction',
                           color_continuous_scale="RdBu_r",
                           range_color=(0, 0.1),
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 40.676649, "lon": -74.009550},
                           opacity=0.5,
                           labels={'prediction':'Gentrification Prediction - RedHook'}
                          )
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


with urlopen('https://gist.githubusercontent.com/akash-y/981a07f9924b2aec750ef05d8f0ded59/raw/c5cc1bbdd2a0a63b5ca1d70eaed3daef0cab623f/ny_gentrification_2018.geojson') as response:
    ny_map = json.load(response)

gentrification_2018_ny = pd.read_csv('https://gist.githubusercontent.com/akash-y/0e6a14fa614aabb16b5b35a5273e44ca/raw/ee7aace5cf795aa005cc563c02be97552633b7da/ny_gentrification_2018.csv')

#Mapping Gentrification for NY - Current Year
fig3 = px.choropleth_mapbox(gentrification_2018_ny, geojson=ny_map,locations = 'geo_id' ,featureidkey="properties.geo_id",color='prediction',
                           color_continuous_scale="RdBu_r",
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           zoom=7, center = {"lat": 40.724576, "lon": -73.916812},
                           opacity=0.5,
                           labels={'prediction':'Gentrification Prediction - NY'}
                          )
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Mapping Residential Evictions for NY - Current Year
with urlopen('https://gist.githubusercontent.com/akash-y/6aa5d1fe4bfecda6b2ba7bd4b918e209/raw/04134738f6cce463f787f8a20dc2a1639e15f64c/ny_zip.geojson') as response:
    ny_zip = json.load(response)

evictions_df = pd.read_csv('https://gist.githubusercontent.com/akash-y/e0ffea12dde217ec49546ffa66461ce5/raw/143edbf60b34e34139545cba079124ed01833652/ny_evictions.csv')

residential_evictions = px.choropleth_mapbox(evictions_df, geojson=ny_zip,locations = 'MODZCTA' ,featureidkey="properties.MODZCTA",color='residential_pctl_score',
                           color_continuous_scale="RdBu_r",
                           range_color=(0, 100),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": 40.724576, "lon": -73.916812},
                           opacity=0.5,
                           labels={'prediction':'Residential Evictions Percentile Score'}
                          )

residential_evictions.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Mapping Commercial Evictions for NY - Current Year
commercial_evictions = px.choropleth_mapbox(evictions_df, geojson=ny_zip,locations = 'MODZCTA' ,featureidkey="properties.MODZCTA",color='commercial_pctl_score',
                           color_continuous_scale="RdBu_r",
                           range_color=(0, 100),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": 40.724576, "lon": -73.916812},
                           opacity=0.5,
                           labels={'prediction':'Commercial Evictions Percentile Score'}
                          )

commercial_evictions.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#Mapping Gentrification Prediction  for Red Hook - 5 Years
redhook_5yr_prediction = pd.read_csv('https://gist.githubusercontent.com/akash-y/4b3e114d2cfdd22aab9462d4db942999/raw/16ae0b48e1094d27a4e3460c3cfb4dda6f047161/redhook_5_gentrification_prediction.csv')

fig4 = px.choropleth_mapbox(redhook_5yr_prediction, geojson=tracts,locations = 'geo_id' ,featureidkey="properties.geo_id",color='prediction',
                           color_continuous_scale="RdBu_r",
                           range_color=(0, 0.1),
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 40.676649, "lon": -74.009550},
                           opacity=0.5,
                           labels={'prediction':'Gentrification Prediction 5 Yrs - RedHook'}
                          )
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#Mapping Gentrification Prediction  for Red Hook - 10 Years
redhook_10yr_prediction = pd.read_csv('https://gist.githubusercontent.com/akash-y/f0a8d865efd78008f49d4f5602ffcf34/raw/1c3f7cb79e521dc3188e817610148ed044dae1b4/redhook_10_gentrification_prediction.csv')

fig5 = px.choropleth_mapbox(redhook_10yr_prediction, geojson=tracts,locations = 'geo_id' ,featureidkey="properties.geo_id",color='prediction',
                           color_continuous_scale="RdBu_r",
                           range_color=(0, 0.1),
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 40.676649, "lon": -74.009550},
                           opacity=0.5,
                           labels={'prediction':'Gentrification Prediction 5 Yrs - RedHook'}
                          )
fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
