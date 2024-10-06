pipeline {
    agent { podman { image 'docker.io/python' } }
    stages {
        stage('build') {
            steps {
                bash 'python --version'
            }
        }
    }
}
