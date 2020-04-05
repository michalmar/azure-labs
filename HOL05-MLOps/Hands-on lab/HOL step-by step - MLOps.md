![Microsoft Cloud Workshops](https://github.com/Microsoft/MCW-Template-Cloud-Workshop/raw/master/Media/ms-cloud-workshop.png "Microsoft Cloud Workshops")

<div class="MCWHeader1">
MLOps
</div>

<div class="MCWHeader2">
Hands-on lab step-by-step
</div>

<div class="MCWHeader3">
November 2019
</div>


Information in this document, including URL and other Internet Web site references, is subject to change without notice. Unless otherwise noted, the example companies, organizations, products, domain names, e-mail addresses, logos, people, places, and events depicted herein are fictitious, and no association with any real company, organization, product, domain name, e-mail address, logo, person, place or event is intended or should be inferred. Complying with all applicable copyright laws is the responsibility of the user. Without limiting the rights under copyright, no part of this document may be reproduced, stored in or introduced into a retrieval system, or transmitted in any form or by any means (electronic, mechanical, photocopying, recording, or otherwise), or for any purpose, without the express written permission of Microsoft Corporation.

Microsoft may have patents, patent applications, trademarks, copyrights, or other intellectual property rights covering subject matter in this document. Except as expressly provided in any written license agreement from Microsoft, the furnishing of this document does not give you any license to these patents, trademarks, copyrights, or other intellectual property.

The names of manufacturers, products, or URLs are provided for informational purposes only and Microsoft makes no representations and warranties, either expressed, implied, or statutory, regarding these manufacturers or the use of the products with any Microsoft technologies. The inclusion of a manufacturer or product does not imply endorsement of Microsoft of the manufacturer or product. Links may be provided to third party sites. Such sites are not under the control of Microsoft and Microsoft is not responsible for the contents of any linked site or any link contained in a linked site, or any changes or updates to such sites. Microsoft is not responsible for webcasting or any other form of transmission received from any linked site. Microsoft is providing these links to you only as a convenience, and the inclusion of any link does not imply endorsement of Microsoft of the site or the products contained therein.

© 2019 Microsoft Corporation. All rights reserved.

Microsoft and the trademarks listed at <https://www.microsoft.com/en-us/legal/intellectualproperty/Trademarks/Usage/General.aspx> are trademarks of the Microsoft group of companies. All other trademarks are property of their respective owners.

**Contents**

<!-- TOC -->

- [MLOps hands-on lab step-by-step](#mlops-hands-on-lab-step-by-step)
  - [Abstract and learning objectives](#abstract-and-learning-objectives)
  - [Overview](#overview)
  - [Solution architecture](#solution-architecture)
  - [Requirements](#requirements)
  - [Before the hands-on lab](#before-the-hands-on-lab)
  - [Exercise 1: Creating and evaluating compliance classification models](#exercise-1-creating-and-evaluating-compliance-classification-models)
    - [Task 1: Create the classification model using a notebook](#task-1-create-the-classification-model-using-a-notebook)
  - [Exercise 2: Registering the model](#exercise-2-registering-the-model)
    - [Task 1: Register Model using Azure Machine Learning Python SDK](#task-1-register-model-using-azure-machine-learning-python-sdk)
    - [Task 2: Register Model from Azure Machine Learning studio](#task-2-register-model-from-azure-machine-learning-studio)
  - [Exercise 3: Setup New Project in Azure DevOps](#exercise-3-setup-new-project-in-azure-devops)
    - [Task 1: Create New Project](#task-1-create-new-project)
    - [Task 2: Import Quickstart code from a GitHub Repo](#task-2-import-quickstart-code-from-a-github-repo)
    - [Task 3: Update the build YAML file](#task-3-update-the-build-yaml-file)
    - [Task 4: Create new Service Connection](#task-4-create-new-service-connection)
  - [Exercise 4: Setup and Run the Build Pipeline](#exercise-4-setup-and-run-the-build-pipeline)
    - [Task 1: Setup Build Pipeline](#task-1-setup-build-pipeline)
    - [Task 2: Run the Build Pipeline](#task-2-run-the-build-pipeline)
    - [Task 3: Review Build Artifacts](#task-3-review-build-artifacts)
    - [Task 4: Review Build Outputs](#task-4-review-build-outputs)
  - [Exercise 5: Setup the Release Pipeline](#exercise-5-setup-the-release-pipeline)
    - [Task 1: Create an Empty Job](#task-1-create-an-empty-job)
    - [Task 2: Add Build Artifact](#task-2-add-build-artifact)
    - [Task 3: Add Variables to Deploy and Test stage](#task-3-add-variables-to-deploy-and-test-stage)
    - [Task 4: Setup Agent Pool for Deploy and Test stage](#task-4-setup-agent-pool-for-deploy-and-test-stage)
    - [Task 5: Add Use Python Version task](#task-5-add-use-python-version-task)
    - [Task 6: Add Install Requirements task](#task-6-add-install-requirements-task)
    - [Task 7: Add Deploy and Test Webservice task](#task-7-add-deploy-and-test-webservice-task)
    - [Task 8: Define Deployment Trigger](#task-8-define-deployment-trigger)
    - [Task 9: Enable Continuous Deployment Trigger](#task-9-enable-continuous-deployment-trigger)
    - [Task 10: Save the Release Pipeline](#task-10-save-the-release-pipeline)
  - [Exercise 6: Test Build and Release Pipelines](#exercise-6-test-build-and-release-pipelines)
    - [Task 1: Make Edits to Source Code](#task-1-make-edits-to-source-code)
    - [Task 2: Monitor Build Pipeline](#task-2-monitor-build-pipeline)
    - [Task 3: Monitor Release Pipeline](#task-3-monitor-release-pipeline)
    - [Task 4: Review Release Pipeline Outputs](#task-4-review-release-pipeline-outputs)
  - [Exercise 7: Testing the deployed solution](#exercise-7-testing-the-deployed-solution)
    - [Task 1: Test the Deployment](#task-1-test-the-deployment)
  - [Exercise 8: Examining deployed model performance](#exercise-8-examining-deployed-model-performance)
    - [Task 1: Activate App Insights and data collection on the deployed model](#task-1-activate-app-insights-and-data-collection-on-the-deployed-model)
    - [Task 2: Check Application Insights telemetry](#task-2-check-application-insights-telemetry)
    - [Task 3: Check the data collected](#task-3-check-the-data-collected)
  - [After the hands-on lab](#after-the-hands-on-lab)
    - [Task 1: Clean up lab resources](#task-1-clean-up-lab-resources)

<!-- /TOC -->

# MLOps hands-on lab step-by-step

## Abstract and learning objectives

In this hands-on lab, you will learn how Trey Research can leverage Deep Learning technologies to scan through their vehicle specification documents to find compliance issues with new regulations. You will standardize the model format to ONNX and observe how this simplifies inference runtime code, enabling pluggability of different models and targeting a broad range of runtime environments, and most importantly, improves inferencing speed over the native model. You will build a DevOps pipeline to coordinate retrieving the latest best model from the model registry, packaging the web application, deploying the web application, and inferencing web service. After a first successful deployment, you will make updates to both the model, the and web application, and execute the pipeline once to achieve an updated deployment. You will also learn how to monitor the model's performance after it is deployed, so Trey Research can be proactive with performance issues.

At the end of this hands-on lab, you will be better able to implement end-to-end solutions that fully operationalize deep learning models, inclusive of all application components that depend on the model.

## Overview

Trey Research Inc. delivers innovative solutions for manufacturers. They specialize in identifying and solving problems for manufacturers that can run the range from automating away mundane but time-intensive processes to delivering cutting edge approaches that provide new opportunities for their manufacturing clients. Trey Research has decades specializing in data science and application development that until now were separate units. They have seen the value created by the ad-hoc synergies between data science and app development, but they would like to unlock the greater, long term value as they formalize their approach by combining the two units into one, and follow one standardized process for operationalizing their innovations.

As their first effort of this combined initiative, they would like to define a process for operationalizing deep learning that encompasses all phases of the application life cycle along with model creation and deployment of a deep learning model. For this first proof of concept (PoC), they would like to focus on component compliance. Specifically, they are looking to leverage Deep Learning technologies with Natural Language Processing (NLP) techniques to scan through vehicle specification documents to find compliance issues with new regulations. Even though this first scenario is focused on vehicle components, they believe this approach will generalize to any scenario involving an inventory of components, which all of their manufacturing customers deal with. The component descriptions, which are free form text, are entered and managed via a web application. This web application will take new component descriptions entered by authorized technicians and label the component as compliant or non-compliant, based on the text.

They want to ensure the overall process they create enables them to update both the underlying model and the web app in one, unified pipeline. They also want to be able to monitor the model's performance after it is deployed so they can be proactive with performance issues.

## Solution architecture

![The lab solution architecture as described by the text that follows.](media/architecture-overview.png 'Solution Architecture')

The overall approach used in this lab is to orchestrate continuous integration and continuous delivery Azure Pipelines from Azure DevOps. These pipelines are triggered by changes to artifacts that describe a machine learning pipeline, that is created with the Azure Machine Learning SDK. In the lab, you make a change to the model training script that executes the Azure Pipelines Build Pipeline, which trains the model and creates the container image. Then this triggers an Azure Pipelines Release pipeline that deploys the model as a web service to AKS, by using the Docker image that was created in the Build pipeline. Once in production, the scoring web service is monitored using a combination of Application Insights and Azure Storage.

## Requirements

1. Microsoft Azure subscription must be pay-as-you-go or MSDN.

    - Trial subscriptions will not work. You will run into issues with Azure resource quota limits.

    - Subscriptions with access limited to a single resource group will not work. You will need the ability to deploy multiple resource groups.

2. An Azure DevOps account.

## Before the hands-on lab

Refer to the [Before the hands-on lab setup guide](./Before&#32;the&#32;HOL&#32;-&#32;MLOps.md) before continuing to the lab exercises.

## Exercise 1: Creating and evaluating compliance classification models

Duration: 40 minutes

In this exercise, you create a model for classifying component text as compliant or non-compliant.

### Task 1: Create the classification model using a notebook

1. Browse to your Azure Notebooks project and navigate to `Deep Learning with Text.ipynb`. This is the notebook you will step through executing in this lab.

2. Follow the instructions within the notebook to complete the lab.

3. In Azure Notebooks, navigate to the `model` folder and download the **model.h5** file to your local disk. We will use the downloaded model file in the next exercise. *Note that if the downloaded file name is changed to `utf-8''model.h5` or `notebooks_model_model.h5`, then rename the file back to `model.h5`*.

    >**Note**: The **model.h5** file is generated during the execution of the notebook at the previous step (step 2). When running the notebook, make sure the execution is successful, and the file is correctly created.

## Exercise 2: Registering the model

Duration: 15 minutes

In this exercise, you explore the approaches you can take to managing the model versions, their association with Experiment Runs, and how you can retrieve the models both programmatically and via the [Azure Machine Learning studio](https://ml.azure.com).

>**Note:** The new [Azure Machine Learning studio](https://ml.azure.com) provides a new immersive experience for managing the end-to-end machine learning lifecycle. You can use it either by logging in directly to it or by selecting the ```Launch the new Azure Machine Learning studio``` option in the ```Overview``` section of your Azure Machine Learning workspace.

### Task 1: Register Model using Azure Machine Learning Python SDK

1. Browse to your Azure Notebooks project and navigate to `Register Model.ipynb`. This is the notebook you will step through executing in this lab.

2. Follow the instructions within the notebook to complete the lab.

3. Log in to [Azure Machine Learning studio](https://ml.azure.com) either directly or via the [Azure Portal](https://portal.azure.com). Make sure you select the Azure Machine Learning workspace that you created from the notebook. Open your **Models** section, and observe the **version 1** of the registered model: `compliance-classifier`.

    ![Review registered model in Azure Portal.](media/model-registry-01.png 'Registered Model: compliance-classifier')

### Task 2: Register Model from Azure Machine Learning studio

1. Log in to [Azure Machine Learning studio](https://ml.azure.com) either directly or via the [Azure Portal](https://portal.azure.com). Make sure you select the Azure Machine Learning workspace that you have created in the previous task. Open your **Models** section and select **Register model**.

    ![Register Model in Azure Machine Learning studio by selecting REgister model in Models section.](media/model-registry-02.png 'Register Model in Azure Machine Learning studio')
  
2. Provide the following input to the `Register a model` dialog, and then select **Register**.

   a. Name: `compliance-classifier`

   b. Description: `Deep learning model to classify the descriptions of car components as compliant or non-compliant.`

   c. Model Framework: `TensorFlow`

   d. Model Framework Version: `2.0`

   e. Model file: Select the `model.h5` file from your local disk.

    ![Register a Model in Azure Machine Learning studio by providing the model file from your local computer.](media/model-registry-03.png 'Register a model Dialog')

3. Navigate to your **Models** section, and observe the **version 2** of the registered model: `compliance-classifier`.

    ![Review the new registered model compliance-classifier version 2 in Azure Machine Learning studio.](media/model-registry-04.png 'Registered Model: compliance-classifier version 2')

## Exercise 3: Setup New Project in Azure DevOps

Duration: 20 minutes

### Task 1: Create New Project

1. Sign in to [Azure DevOps](http://dev.azure.com).

2. Select **New project**.

    ![Create new project in Azure DevOPs.](media/devops-project-01.png 'Create new project')

3. Provide Project Name: `mlops-quickstart` and select **Create**.

    ![Provide project name in the create new project dialog and then select create.](media/devops-project-02.png 'Create New Project Dialog')

### Task 2: Import Quickstart code from a GitHub Repo

1. Within the new project:

   a. Select **Repos** from left navigation bar.

   b. Select **Import** from the content section.

    ![Import Quickstart code from a GitHub Repo.](media/devops-project-03.png 'Azure DevOps Repos')

2. Provide the following GitHub URL: `https://github.com/solliancenet/mcw-mlops-starter` and select **Import**. This should import the code required for the quickstart.

    ![Provide the above GitHub URL and select import to import the source code.](media/devops-project-04.png 'Import a Git repository dialog')

    *Note that if you receive an error while importing the repository, please disable the preview feature `New Repos landing pages` and import the GitHub repository from the old UI, as shown in steps #3, #4, and #5 below.*

3. [Optional] Select **Account settings, Preview features**.

    ![The image shows how to navigate to the list of preview features.](media/preview_features-01.png 'Preview features')

4. [Optional] From the list of preview features, disable the preview feature **New Repos landing pages**.

   ![The image shows a list of preview features and highlights the preview feature, New Repos landing pages.](media/preview_features-02.png 'Disable New Repos landing pages')

5. [Optional] Repeat Step #1 above to import the GitHub repository from the old UI.

### Task 3: Update the build YAML file

1. Select and open the `azure-pipelines.yml` file.

2. Select **Edit** and update the following variables: `resourcegroup`, and `workspace`. If you are using your own Azure subscription, please provide names to use. If an environment is provided to you, be sure to replace XXXXX in the values below with your unique identifier.

    ![Edit build YAML file and provide your resource group and workspace information.](media/devops-build-pipeline-01.png 'Edit Build YAML file')

3. Select **Commit** to save your changes.

    ![Commit your changes to the build YAML file.](media/devops-build-pipeline-02.png 'Commit Build YAML file')
  
### Task 4: Create new Service Connection

1. From the left navigation, select **Project settings** and then select **Service connections**.

    ![Navigate to Project Settings, Service connections section.](media/devops-build-pipeline-03.png 'Service Connections')

2. Select **Create service connection**, select **Azure Resource Manager**, and then select **Next**.

    ![Select Create Service Connection, Azure Resource Manager.](media/devops-build-pipeline-04.png 'Azure Resource Manager')

3. Select **Service principal (automatic)** and then select **Next**.

    ![Select Service principal (automatic), and then select Next.](media/devops-build-pipeline-05.png 'Service principal authentication')

4. Provide the following information in the `New Azure service connection` dialog box and then select **Save**:

    a. Type: `Machine Learning Workspace`

    b. Subscription: Select the Azure subscription to use.

    > **Note**: It might take up to 30 seconds for the **Subscription** dropdown to be populated with available subscriptions, depending on the number of different subscriptions your account has access to.

    c. Resource group: This value should match the value you provided in the `azure-pipelines.yml` file.

    d. Machine Learning Workspace: This value should match the value you provided in the `azure-pipelines.yml` file.

    e. Service connection name: `quick-starts-sc`

    f. Grant access permission to all pipelines: this checkbox must be selected.

    ![Provide connection name, Azure Resource Group, Machine Learning Workspace, and then select Save. The resource group and machine learning workspace must match the value you provided in the YAML file.](media/devops-build-pipeline-06.png 'Add an Azure Resource Manager service connection dialog')

## Exercise 4: Setup and Run the Build Pipeline

Duration: 25 minutes

> **Note**: This exercise requires the new version of the **Pipelines** user interface. To activate it, select **Pipelines** from the left navigation. If the first option below **Pipelines** is **Builds**, you are still running on the previous version of the user interface. In this case, a popup should appear suggesting the activation of the new user interface.
>
> ![Activate the new Azure Pipelines user interface.](media/devops-ui-activation.png 'Multi-stage pipelines activation')
>
> Select **Try it!** to activate the new Pipelines user interface. When successfully activated, the first option below **Pipelines** from the left navigation will change to **Pipelines**.

### Task 1: Setup Build Pipeline

1. From left navigation select **Pipelines, Pipelines** and then select **Create pipeline**.

    ![Navigate to Pipelines, Pipelines, and then select Create pipeline](media/devops-build-pipeline-07.png 'Create Build Pipeline')

2. Select **Azure Repos Git** as your code repository.

    ![Select your code repository source for your new build pipeline.](media/devops-build-pipeline-08.png 'Repository Source')

3. Select **mlops-quickstart** as your repository.

    ![Select mlops-quickstart as your repository.](media/devops-build-pipeline-09.png 'Select Repository')

4. Review the YAML file.

    The build pipeline has four key steps:

    a. Attach folder to workspace and experiment. This command creates the `.azureml` subdirectory that contains a `config.json` file that is used to communicate with your Azure Machine Learning workspace. All subsequent steps rely on the `config.json` file to instantiate the workspace object.

    b. Create the AML Compute target to run your master pipeline for model training and model evaluation.

    c. Run the master pipeline. The master pipeline has two steps: (1) Train the machine learning model, and (2) Evaluate the trained machine learning model. The evaluation step evaluates if the new model performance is better than the currently deployed model. If the new model performance is improved, the evaluate step will create a new Image for deployment. The results of the evaluation step will be saved in a file called `eval_info.json` that will be made available for the release pipeline. You can review the code for the master pipeline and its steps in `aml_service/pipelines_master.py`,  `scripts/train.py`, and `scripts/evaluate.py`.

    d. Publish the build artifacts. The `snapshot of the repository`, `config.json`, and `eval_info.json` files are published as build artifacts and thus can be made available for the release pipeline.

    ![Review the build pipeline YAML file.](media/devops-build-pipeline-10.png 'Build pipeline YAML')

### Task 2: Run the Build Pipeline

1. Select **Run** to start running your build pipeline.

    ![Start the run for your build pipeline.](media/devops-build-pipeline-11.png 'Run Build Pipeline')

2. Monitor the build run. The build pipeline, for the first run, will take around 15 minutes to run.

    ![Monitor your build pipeline. It will take around 15 minutes to run.](media/devops-build-pipeline-12.png 'Monitor Build Pipeline')

3. Select **Job** to monitor the detailed status of the build pipeline execution.

    ![Monitor the details of your build pipeline.](media/devops-build-pipeline-13.png 'Monitor Build Pipeline Details')

### Task 3: Review Build Artifacts

1. The build will publish an artifact named `devops-for-ai`. Select **Artifacts, 1 published** to review the artifact contents.

    ![Select Artifacts, 1 published to review the artifact contents.](media/devops-build-pipeline-14.png 'Build Artifacts')

2. Select **outputs, eval_info.json**, and then select the download arrow. The `eval_info.json` is the output from the *model evaluation* step. The information from the evaluation step will be used in the release pipeline to deploy the model. Select the back arrow to return to the previous screen.

    ![Download output from the model evaluation step.](media/devops-build-pipeline-15.png 'Download JSON file')

3. Open the `eval_info.json` in a json viewer or a text editor and observe the information. The json output contains information such as if the model passed the evaluation step (`deploy_model`: *true or false*), and the name and id of the created image (`image_name` and `image_id`) to deploy.

    ![Review information in the eval_info json file.](media/devops-build-pipeline-16.png 'Eval Info JSON File')

### Task 4: Review Build Outputs

1. Log in to [Azure Machine Learning studio](https://ml.azure.com) either directly or via the [Azure Portal](https://portal.azure.com). Make sure you select the Azure Machine Learning workspace that you created from the notebook earlier. Open your **Models** section, and observe the versions of the registered model: `compliance-classifier`. The latest version is the one registered by the build pipeline you ran in the previous task.

    ![Review registered model in Azure Machine Learning studio.](media/devops-build-outputs-01.png 'Registered Models in Azure Machine Learning studio')

2. Select the latest version of your model to review its properties. The ```build_number``` tag links the registered model to the Azure DevOps build that generated it.

    ![Review registered model properties, notice Build_Number tag.](!media/../media/devops-build-outputs-02.png 'Registered model details and Build_Number tag')

3. Open your **Datasets** section and observe the versions of the registered dataset: ```connected_car_components```. The latest version is the one registered by the build pipeline you have run in the previous task.

    ![Review registered dataset in Azure Machine Learning studio.](media/devops-build-outputs-03.png 'Registered Datasets in Azure Machine Learning studio')

4. Select the latest version of your dataset to review its properties. Notice the ```build_number``` tag that links the dataset version to the Azure DevOps build that generated it.

    ![Review registered dataset version properties, notice Build_Number tag.](medial/../media/devops-build-outputs-04.png 'Registered dataset details in Azure Machine Learning studio')

5. Select **Models** to view a list of registered models that reference the dataset.

    ![Review list of registered models that reference dataset in Azure Machine Learning studio.](media/devops-build-outputs-05.png 'Registered dataset model references in Azure Machine Learning studio')

6. Log in to the [Azure Portal](https://portal.azure.com), open your **Resource Group, Workspace, Images** section, and observe the deployment image created during the build pipeline: `compliance-classifier-image`.

    ![Review deployment image in Azure Portal.](media/devops-build-outputs-06.png 'Images in Azure Portal')

## Exercise 5: Setup the Release Pipeline

Duration: 20 minutes

### Task 1: Create an Empty Job

1. Return to Azure DevOps and navigate to **Pipelines, Releases** and select **New pipeline**.

    ![To create new Release Pipeline navigate to Pipelines, Releases and select New pipeline.](media/devops-release-pipeline-01.png 'New Release Pipeline')

2. Select **Empty job**.

    ![Select empty job to start building the release pipeline.](media/devops-release-pipeline-02.png 'Select a template: Empty job')

3. Provide Stage name: `Deploy and Test` and close the dialog.

    ![Provide stage name for the release stage.](media/devops-release-pipeline-03.png 'Deploy and Test Stage')

### Task 2: Add Build Artifact

1. Select **Add an artifact**.

    ![Add a new artifact to the release pipeline.](media/devops-release-pipeline-04.png 'Add an artifact')

2. Select Source type: `Build`, Source (build pipeline): `mlops-quickstart`. *Observe the note that shows that the mlops-quickstart publishes the build artifact named devops-for-ai*. Finally, select **Add**.

    ![Provide information to add the build artifact.](media/devops-release-pipeline-05.png 'Add a build artifact')

### Task 3: Add Variables to Deploy and Test stage

1. Open **View stage tasks** link.

    ![Open view stage tasks link.](media/devops-release-pipeline-06.png 'View Stage Tasks')

2. Open the **Variables** tab.

    ![Open variables tab.](media/devops-release-pipeline-07.png 'Release Pipeline Variables')

3. Add four Pipeline variables as name - value pairs and then select **Save** (use the default values in the **Save** dialog):

    a. Name: `aks_name` Value: `aks-cluster01`

    b. Name: `aks_region` Value: `eastus`

    c. Name: `service_name` Value: `compliance-classifier-service`

    d. Name: `description` Value: `"Compliance Classifier Web Service"` *Note the double quotes around description value*.

    >**Note**:
    >- Keep the scope for the variables to `Deploy and Test` stage.
    >- The name of the Azure region should be the same one that was used to create Azure Machine Learning workspace earlier on.

      ![Add four pipeline variables as name value pairs and save.](media/devops-release-pipeline-08.png 'Add Pipeline Variables')

### Task 4: Setup Agent Pool for Deploy and Test stage

1. Open the **Tasks** tab.

    ![Open view stage tasks link.](media/devops-release-pipeline-09.png 'Pipeline Tasks')

2. Select **Agent job** and change **Agent pool** to `Azure Pipelines` and change **Agent Specification** to `ubuntu-16.04`.

    ![Change Agent pool to be Hosted Ubuntu 1604.](media/devops-release-pipeline-10.png 'Agent Job Setup')

### Task 5: Add Use Python Version task

1. Select **Add a task to Agent job** (the **+** button), search for `Use Python Version`, and select **Add**.

    ![Add Use Python Version task to Agent job.](media/devops-release-pipeline-11.png 'Add Use Python Version Task')

2. Provide **Display name:** `Use Python 3.6` and **Version spec:** `3.6`.

    ![Provide Display name and Version spec for the Use Python version task.](media/devops-release-pipeline-12.png 'Use Python Version Task Dialog')

### Task 6: Add Install Requirements task

1. Select **Add a task to Agent job** (the **+** button), search for `Bash`, and select **Add**.

    ![Add Bash task to Agent job.](media/devops-release-pipeline-13.png 'Add Bash Task')

2. Provide **Display name:** `Install Requirements` and select **object browser ...** to provide **Script Path**.

    ![Provide Display name for the Bash task.](media/devops-release-pipeline-14.png 'Bash Task Dialog')

3. Navigate to **Linked artifacts/_mlops-quickstart (Build)/devops-for-ai/environment_setup** and select **install_requirements.sh**.

    ![Provide Script Path to the Install Requirements bash file.](media/devops-release-pipeline-15.png 'Select Path Dialog')

4. Expand **Advanced** and select **object browser ...** to provide **Working Directory**.

    ![Expand advanced section to provide Working Directory.](media/devops-release-pipeline-16.png 'Bash Task - Advanced Section')

5. Navigate to **Linked artifacts/_mlops-quickstart (Build)/devops-for-ai** and select **environment_setup**.

    ![Provide path to the Working Directory.](media/devops-release-pipeline-17.png 'Select Path Dialog')

### Task 7: Add Deploy and Test Webservice task

1. Select **Add a task to Agent job** (the **+** button), search for `Azure CLI`, and select **Add**.

    ![Add Azure CLI task to Agent job.](media/devops-release-pipeline-18.png 'Azure CLI Task')

2. Provide the following information for the Azure CLI task:

    a. Display name: `Deploy and Test Webservice`

    b. Azure subscription: `quick-starts-sc` *This is the service connection we created in Exercise 1 / Task 4*.

    c. Script Location: `Inline script`

    d. Inline Script: `python aml_service/deploy.py --service_name $(service_name) --aks_name $(aks_name) --aks_region $(aks_region) --description $(description)`

    ![Setup the Azure CLI task using the information above.](media/devops-release-pipeline-19.png 'Azure CLI Task Dialog')

3. Expand **Advanced** and provide **Working Directory:** `$(System.DefaultWorkingDirectory)/_mlops-quickstart/devops-for-ai`.

    ![Provide Working Directory for the Azure CLI task.](media/devops-release-pipeline-20.png 'Azure CLI Task - Working Directory')

Please review the code in `aml_service/deploy.py`. This step will read the `eval_info.json`, and if the evaluation step recommended to deploy the new trained model, it will deploy the new model to production in an **Azure Kubernetes Service (AKS)** cluster.

### Task 8: Define Deployment Trigger

1. Navigate to **Pipeline** tab, and select **Pre-deployment conditions** for the `Deploy and Test` stage.

2. Select **After release**.

    ![Setup Pre-deployment conditions for the Deploy and Test stage.](media/devops-release-pipeline-21.png 'Pre-deployment Conditions Dialog')

3. Close the dialog.

### Task 9: Enable Continuous Deployment Trigger

1. Select **Continuous deployment trigger** for `_mlops-quickstart` artifact.

2. Enable: **Creates a release every time a new build is available**.

    ![Enable Continuous Deployment Trigger for the Release pipeline.](media/devops-release-pipeline-22.png 'Continuous Deployment Trigger Dialog')

3. Close the dialog

### Task 10: Save the Release Pipeline

1. Provide name: `mlops-quickstart-release`.

2. Select: **Save** (use the default values in the **Save** dialog).

    ![Provide name for the release pipeline and select save.](media/devops-release-pipeline-23.png 'Save')

## Exercise 6: Test Build and Release Pipelines

Duration: 30 minutes

### Task 1: Make Edits to Source Code

1. Navigate to: **Repos -> Files -> scripts -> `train.py`**.

2. **Edit** `train.py`.

3. Change the **learning rate (lr)** for the optimizer from **0.1** to **0.001**.

4. Change the number of training **epochs** from **3** to **5**.

5. Select **Commit**.

    ![Make edits to train.py by changing the learning rate. Select Commit after editing.](media/devops-test-pipelines-01.png 'Edit Train.py')

6. Provide comment: `Improving model performance: changed learning rate.` and select **Commit**.

    ![Provide commit comment for train.py.](media/devops-test-pipelines-02.png 'Commit - Comment')

### Task 2: Monitor Build Pipeline

1. Navigate to **Pipelines, Pipelines**. Observe that the CI build is triggered because of the source code change.

   ![Navigate to Pipelines, Builds.](media/devops-test-pipelines-03.png 'Pipelines - pipelines')

2. Select the pipeline run and monitor the pipeline steps. The pipeline will run for 16-18 minutes. Proceed to the next task when the build pipeline successfully completes.

   ![Monitor Build Pipeline. It will take around 15 minutes to complete.](media/devops-test-pipelines-04.png 'Build Pipeline Steps')

### Task 3: Monitor Release Pipeline

1. Navigate to **Pipelines, Releases**. Observe that the Release pipeline is automatically triggered upon successful completion of the build pipeline. Select as shown in the figure to view pipeline logs.

   ![Navigate to Pipelines, Releases and Select as shown in the figure to view pipeline logs.](media/devops-test-pipelines-05.png 'Pipelines - Releases')

2. The release pipeline will run for about 15 minutes. Proceed to the next task when the release pipeline successfully completes.

### Task 4: Review Release Pipeline Outputs

1. From the pipeline logs view, select **Deploy and Test Webservice** task to view details.

    ![Select Deploy and Test Webservice task to view details.](media/devops-test-pipelines-06.png 'Pipeline Logs')

2. Observe the **Scoring URI** and **API Key** for the deployed webservice. Please note down both the `Scoring URI` and `API Key` for *Exercise 7*.

    ![View Deploy and Test Webservice task logs and note down the Scoring URI of the deployed webservice.](media/devops-test-pipelines-07.png 'Deploy and Test Webservice Task Logs')

3. Log in to Azure Machine Learning studio. Open your **Endpoints** section, and observe the deployed webservice: **compliance-classifier-service**.

    ![View deployed webservice in Azure Machine Learning studio.](media/devops-test-pipelines-08.png 'Azure Machine Learning studio - Workspace, Deployments')

## Exercise 7: Testing the deployed solution

Duration: 15 minutes

In this exercise, you verify that the first release of the application works.

### Task 1: Test the Deployment

1. Browse to your Azure Notebooks project and navigate to `Test Deployment.ipynb`. This is the notebook you will step through executing in this lab.

2. Follow the instructions within the notebook to complete the lab.

3. Note that you will have to provide values for **Scoring URI** and **API Key** for the deployed webservice in the notebook.

## Exercise 8: Examining deployed model performance

Duration: 15 minutes

In this exercise, you learn how to monitor the performance of a deployed model.

### Task 1: Activate App Insights and data collection on the deployed model

1. Browse to your Azure Notebooks project and navigate to the [Model Telemetry](notebooks/Model%20Telemetry.ipynb) notebook. This is the notebook you will step through executing in this task.

2. Follow the instructions within the notebook to complete the task. When finished, your deployed model has now both [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) integration and data collection activated.

3. Note that if there are errors (for example, `Too many requests for service compliance-classifier-service (overloaded)`) when you make calls against the deployed web service after your enable app insights (last cell in the `Model Telemetry` notebook), you should wait for 5 minutes and rerun the cell to make the calls.

### Task 2: Check Application Insights telemetry

1. Navigate to the Azure Portal and locate the resource group you created for this lab (the one where the Azure Machine Learning service workspace was created in).

2. Locate the Application Insights instance in the resource group and select it.

    ![Application Insights instance in resource group.](media/model-telemetry-01.png 'Resource Group Overview')

3. Go to **Overview**.

4. From the top row of the right section, select **Logs (Analytics)**. This will open the Application Insights query editor with an empty new query.

    ![From Application Insights Dashboard, select Logs to open the Query Editor.](media/model-telemetry-02.png 'Application Insights - Dashboard')

5. In the left pane, make sure the **Schema** tab is selected.

6. Hover over **requests** and select the icon on the right side - "Show sample records from this table".

    ![In Application Insights create requests query.](media/model-telemetry-03.png 'Create Requests Query')

7. Look at the results displayed. Application Insights is tracing all requests made to your model. Sometimes, a couple of minutes are needed for the telemetry information to propagate. If there are no results displayed, wait a minute. Call your model wait a minute and select **Run** to re-execute the Application Insights query.

   ![In Application Insights observe requests query results.](media/model-telemetry-04.png 'Requests Query Results')

*Note that if you do not see telemetry information after selecting **Run** to re-execute the Application insights query. Please rerun the last cell in the `Model Telemetry` notebook a few more times to generate more data. Then select **Run** on this page to re-execute the Application insights query.*

### Task 3: Check the data collected

1. Navigate to the Azure Portal and locate the resource group you created for this lab (the one where the Azure Machine Learning service workspace was created in).
2. Locate the Storage Account instance in the resource group and select it.

    ![From the Resource Group Overview locate the Telemetry Storage account](media/model-telemetry-05.png 'Resource Group Overview')

3. Go to **Storage Explorer (preview)**.

4. Expand the **BLOB CONTAINERS** section and identify the **modeldata** container. Select **More->Refresh** if you do not see **modeldata** container.

    ![Locate the telemetry blob container in the storage account.](media/model-telemetry-06.png 'Storage Explorer')

5. Identify the CSV files containing the collected data. The path to the output blobs is based on the following structure:

    `modeldata -> subscriptionid -> resourcegroup -> workspace -> webservice -> model -> version -> identifier -> year -> month -> day -> data.csv`

    ![Locate telemetry data in the blob container.](media/model-telemetry-07.png 'Storage Explorer - data.csv')

## After the hands-on lab

Duration: 5 minutes

To avoid unexpected charges, it is recommended that you clean up all of your lab resources when you complete the lab.

### Task 1: Clean up lab resources

1. Navigate to the Azure Portal and locate the resource group you created for this lab (the one where the Azure Machine Learning service workspace was created in).

2. Select **Delete resource group** from the command bar.

    ![Screenshot of the Delete resource group button.](media/cleanup-01.png 'Delete resource group button')

3. In the confirmation dialog that appears, enter the name of the resource group and select **Delete**.

4. Wait for the confirmation that the Resource Group has been successfully deleted. If you don't wait, and the delete fails for some reason, you may be left with resources running that were not expected. You can monitor using the Notifications dialog, which is accessible from the Alarm icon.

    ![The Notifications dialog box has a message stating that the resource group is being deleted.](media/cleanup-02.png 'Delete Resource Group Notification Dialog')

5. When the Notification indicates success, the cleanup is complete.

    ![The Notifications dialog box has a message stating that the resource group has been deleted.](media/cleanup-03.png 'Delete Resource Group Notification Dialog')

You should follow all steps provided _after_ attending the Hands-on lab.
