
<p align="center"><h1 align="center">ECONOMETRIA</h1></p>
<p align="center">
	<em>Using ARIMA models for time series analysis.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/daniel-strauss/econometria?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/daniel-strauss/econometria?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/daniel-strauss/econometria?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

### [$\rightarrow$ Click here to see the project report $\leftarrow$](report/Econometria_final_project.pdf)

##  Table of Contents

- [ Overview](#-overview)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
---

##  Overview

Will the sun rise up tomorrow? Many people believe the sun will rise tomorrow since it rose every last
day of their lives. Is that a logical conclusion? At least empirically seen, on every past day of their lives,
it was more useful to predict the sun would do that thing the next morning than it did all days in their
life before that past day. But is it logical to conclude that if a conclusion proved to be useful on every past
day of one’s life, it would be useful today? It can be seen, that we end up at the initial problem. To not turn crazy, let’s just make that conclusion, independent
of whether it is logical or not. Carefully picking some things to assume to be time-invariant leaves us
with a new ability: making predictions about the future from observations in the past. For example, one
could pick, as such, the stationarity of a time series. If one wants to predict a time series $W_t$ that takes
algebraic values, such information about the future may lie in estimated autocorrelations and partial
autocorrelations observed from the past. If this series is stationary, the correlations will repeat in the
future. Empirically, we can not prove stationarity, but we can observe statistically significant stationarity.
How can we use this knowledge to exploit autocorrelations and partial autocorrelations best for future
predictions? In the course Econometria II, we learned about the theory and the practical usage of
ARIMA models. ARIMA models are a family of models capable of expressing autocorrelation and partial
autocorrelation functions (ACF and PACF) of a time series’s stationary and invertible differentiation.
This project aimed to model and validate a real-life time series with an ARIMA model.

##  Project Structure

```sh
└── econometria/
    ├── data
    │   ├── 61111-0002_de.csv
    │   ├── 61111-0002_de.zip
    │   ├── 61111-0002_de_flat.csv
    │   ├── 61111-0002_de_flat.zip
    │   ├── AirPassengers.csv
    │   ├── Coca-Cola_Stock_Price_History.csv
    │   ├── DAX_Historical_Data.csv
    │   ├── DAX_Historical_Data_2_year_daily.csv
    │   ├── DAX_Historical_Data_monthly.csv
    │   ├── EUR_USD_monthly.csv
    │   ├── IPC.csv
    │   ├── IPE.csv
    │   ├── IPE_2.csv
    │   ├── S_P_500_Historical_Data.csv
    │   ├── US_Dollar_Index_Historical_Data.csv
    │   ├── WWWusage.csv
    │   ├── csv_s33-bruttoinlandsprodukt.csv
    │   ├── future-gc00-daily-prices.csv
    │   ├── shampoo.csv
    │   └── unemployed_germany_monthly.csv
    ├── jupyter_pdfs
    │   ├── HELPER_CODE_project_final.pdf
    │   ├── IPC_analysis_BOXCOX.pdf
    │   ├── IPC_analysis_LOG.pdf
    │   ├── IPE_analysis.pdf
    │   ├── all_auto.pdf
    │   └── project_final_clean.pdf
    ├── report
    │   ├── Econometria_final_project.pdf
    │   └── presentation_projecto_final.pdf
    └── src
        ├── HELPER_CODE_project_final.ipynb
        ├── IPC_analysis_BOXCOX.ipynb
        ├── IPC_analysis_LOG.ipynb
        ├── IPE_analysis.ipynb
        ├── all_auto.ipynb
        └── project_final_clean.ipynb
```


###  Project Index
<details open>
	<summary><b><code>ECONOMETRIA/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/daniel-strauss/econometria/blob/master/src/IPC_analysis_LOG.ipynb'>IPC_analysis_LOG.ipynb</a></b></td>
				<td>- The file `src/IPC_analysis_LOG.ipynb` is a Jupyter notebook that is part of the larger codebase<br>- This file is primarily used for Inter-Process Communication (IPC) analysis<br>- It is a key component in the project's data analysis and visualization layer, providing valuable insights into the communication between different processes in the system<br>- The notebook's main purpose is to analyze and visualize IPC data, which is crucial for understanding the system's performance and identifying potential bottlenecks or issues<br>- This analysis can help in optimizing the system's performance and ensuring smooth and efficient communication between different processes<br>- In the context of the entire project structure, this file is located in the `src` directory, indicating that it is part of the source code of the project<br>- It is likely used in conjunction with other files in the `src` directory to perform comprehensive data analysis and visualization tasks.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/daniel-strauss/econometria/blob/master/src/IPE_analysis.ipynb'>IPE_analysis.ipynb</a></b></td>
				<td>- The file `src/IPE_analysis.ipynb` is a Jupyter notebook that forms a crucial part of the project's codebase<br>- It is primarily used for the analysis of Inter-Processor Events (IPE) within the system<br>- The notebook contains code cells that perform various data processing and analytical tasks on the IPE data<br>- In the context of the entire project, this file is responsible for providing insights and understanding about the inter-processor events, which can be used to optimize the system's performance, identify bottlenecks, and troubleshoot issues<br>- The results from this analysis can influence decision-making and strategic planning for the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/daniel-strauss/econometria/blob/master/src/project_final_clean.ipynb'>project_final_clean.ipynb</a></b></td>
				<td>- The file `src/project_final_clean.ipynb` is a Jupyter notebook that forms a crucial part of the project's codebase<br>- This file is primarily responsible for the final processing and cleaning of the project's data<br>- It is likely to contain a series of data manipulation and cleaning steps, which ensure that the data is in the correct format and free from errors or inconsistencies before it is used in subsequent stages of the project<br>- This file is essential for maintaining the integrity and reliability of the project's data, and by extension, the validity of the project's overall results.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/daniel-strauss/econometria/blob/master/src/HELPER_CODE_project_final.ipynb'>HELPER_CODE_project_final.ipynb</a></b></td>
				<td>- The file 'src/HELPER_CODE_project_final.ipynb' is a Jupyter notebook that serves as a crucial component of the project's codebase<br>- It is primarily designed to provide auxiliary functions and routines that support the main functionalities of the project<br>- These helper functions could range from data preprocessing, error handling, to utility functions that enhance code reusability and maintainability<br>- In the context of the entire codebase architecture, this file is likely to be imported or called by other scripts or notebooks in the project, thereby facilitating smoother and more efficient execution of the project's primary tasks<br>- It's a key piece in the overall project structure, contributing to the modularity and organization of the codebase.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/daniel-strauss/econometria/blob/master/src/IPC_analysis_BOXCOX.ipynb'>IPC_analysis_BOXCOX.ipynb</a></b></td>
				<td>- The file `src/IPC_analysis_BOXCOX.ipynb` is a Jupyter notebook that is part of the larger codebase<br>- This file is primarily used for conducting an Inter-Process Communication (IPC) analysis using the Box-Cox transformation method<br>- The Box-Cox transformation is a statistical technique used to make non-normal distribution data normal<br>- This is crucial in many statistical models which require the data to be normally distributed<br>- In the context of the entire project, this file's purpose is to ensure that the data being used in other parts of the codebase is suitable for those processes<br>- It's a key part of the data preprocessing stage, ensuring the data is in the right format and condition to be used effectively in subsequent stages of the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/daniel-strauss/econometria/blob/master/src/all_auto.ipynb'>all_auto.ipynb</a></b></td>
				<td>- The file `src/all_auto.ipynb` is a Jupyter notebook that forms a crucial part of the project's codebase<br>- It appears to be responsible for executing a series of tasks or computations, as suggested by the "ExecuteTime" metadata<br>- The exact nature of these tasks is not clear from the provided information, but given the file's location and name, it might be involved in automating certain processes across the entire project<br>- This could include tasks like data processing, model training, or report generation<br>- The notebook's outputs likely contribute to the overall functionality and results of the project.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
### References

Spyros Makridakis, Steven C Wheelwright, and Rob J Hyndman. Forecasting methods and appli-
cations. John wiley & sons, 2008


