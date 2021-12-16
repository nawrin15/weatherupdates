#!/bin/bash
echo "Setup setupsentiai web"
pathToSentimentanalysisCore=`pwd`
echo $pathToSentimentanalysisCore
cd ../sentiAI/
pathToSentiaiWeb=`pwd`
cd $pathToSentimentanalysisCore
pathToIntegration=./deploy/files/integration
chmod 700 $pathToIntegration/setupsentimentanalysiswebtie.sh $pathToIntegration/renamepath.sh
$pathToIntegration/setupsentimentanalysiswebtie.sh $pathToSentiaiWeb $pathToSentimentanalysisCore
$pathToIntegration/renamepath.sh $pathToSentimentanalysisCore 'assets\/' 'static\/sentimentanalysiswebtie\/assets'
