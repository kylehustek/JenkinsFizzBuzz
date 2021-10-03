pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo "Getting Code:"
                script{
                    git branch: 'fizz',
                    credentialsId: 'dc532151-5d0c-454b-9693-05d87fbe3fd5',
                    url: 'https://kylehustek@github.com/kylehustek/JenkinsFizzBuzz.git'
                }
                echo "finished"
            }
        }
        stage ('Lint Python Files'){
            steps {
                sh 'pylint --output-format=text $(find . -type f -name "*.py") > pylint.log || echo pylint exited with code $?'
            }
        }
        stage ('Test Python Files'){
            steps {
                sh 'pytest > pytest.log'
            }
        }
    }
}