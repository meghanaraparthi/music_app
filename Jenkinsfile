pipeline { 
    agent any 

    stages { 
        stage('Build Docker Image') { 
            steps { 
                echo "Building Docker Image..."
                bat "docker build -t sreeja20082004/sample:v1 ." //change with ur username of dockerhub and container name
            } 
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u sreeja20082004 -p <YOUR_DOCKERHUB_PASSWORD>' //change with ur dockerhub username and password
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                bat "docker push sreeja20082004/sample:v1" //change
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post { 
        success { 
            echo '✅ Pipeline completed successfully! App deployed to Kubernetes.'
        } 
        failure { 
            echo '❌ Pipeline failed. Please check the logs for details.' 
        } 
    } 
}
