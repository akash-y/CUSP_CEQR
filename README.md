# CUSP_CEQR

## Digital CEQR 2.0 : Making real-time predictions for city planning proposals. 

### Akash Yadav, Guilherme Louzada, Eric Zhuang and Chenjie Su.

City Environmental Quality Review (CEQR) is a process that needs to be executed should any urban project may have an impact on the city's environment. Currently, the majority of the environmental analysis work is done manually by the employees from different NYC government departments with specific chapters assigned to. Manual environmental analysis requires tons of work hours, resources and communication between various private and public entities. InCitu came up with a great idea of using predictive analytics to increase the efficiency and accuracy of CEQR analysis. 

Focusing on Chapter 5 : Socioeconomic Conditions of the CEQR Environmental Review Process, we build an analysis freamework to accurately predict the risk of commerical and residential displacement within a neighborhood. We do so by calculating risks of gentrification, eviction and changing dynamics of the macro economic environment. The datasets used for the purpose includes the ACS 5 year survey, Social Vulnerability Index, Annualised Home Sale Prices, Zillow's Median Rental Prices Dataset and NYC Open Data on Legally Operating Businesses and Evictions. 

In order to ease the decisioning process for CEQR officials, we developed a visualization tool to show the results of this project. By accessing the page of the tool it is possible to select the visualization showing the trends of each one of the five factors described above. Also, on the page, we added the conclusion of the analysis for the Red Hook area, which is an area of interest to the sponsors of this project. It is worth noting that this is a minimum viable product version of the proposed tool, we believe further versions of this tool could be developed incorporating the analysis for other regions, so the work could be generalized.

### Execution Steps

1. All data used for the project is available online and can be found here : https://drive.google.com/drive/folders/1ZYRsu_MPOeYv4xvpis3i5XB84rJaAQse?usp=sharing
2. In order to get started with predicting gentrification, run the Gentrification_Labels.ipynb file to generate gentrification labels for the time-period you wish to investigate. 
3. Save results of the gentrification labels in a CSV and use them in the Gentrification_Prediction.ipynb file. Run the Gentrification_Prediction.ipynb file to generate prediction results using ACS and SVI data. 
4. Run CEQR.ipynb to generate CEQR projects in the area you are interested to study
5. Run Price_Predictions.ipynb, Business_Displacement.ipynb and Evictions.ipynb for the entirety of New York City or a particular area of study. All data has been spatially indexed within the notebooks to allow for ease of matching with CEQR project locations
6. Use Demographic_Prediction_Simulations.ipynb to simulate demographic predictions for any future year and use them as results for the Gentrification Prediction Task.
7. Visualise all the data using the tool avaialble here : https://github.com/guiml/NYU2020_Dashboard

All Prediction tasks are available in the Notebooks Folder. Results for NYC and Redhook are available as CSV files in the Results folder and all spatial data files are avaialble in the Shapefiles folder. 

#### What are the advantages of using CEQR Tool over traditional early warning systems or current DCP outlined methods?

It is our understanding that other analyses have previously produced similar results but still, we could not find other tools that cover the many different aspects of CEQR decision process in one frame as we did. It is worth noting that the CEQR process itself does not use a macro approach(such as racial variables) and have rules that are considered flawed, some of which we found in the literature review. We believe our tool addressed these issues more consistently when compared to similar studies in this area. The findings of this research suggest that change in income and ethnicity related factors play important roles in predicting neighborhood gentrification risk. Since the city agencies currently only use project-specific CEQR analysis but excluding macro demographic and economic factors, our results can potentially provide them with a better understanding of city-wide displacement risk during the decision making process.

#### Link to paper : https://docdro.id/v3jqF8O
