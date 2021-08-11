{{- define "experiment2.name" }}
{{- default .Chart.Name | quote }}
{{- end }}