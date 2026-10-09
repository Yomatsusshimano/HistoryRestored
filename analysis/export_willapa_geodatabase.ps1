param(
    [string]$DatabasePath = 'tmp/research/WC46C03.mdb',
    [string]$OutputPath = 'data/willapa-geodatabase-rows.json'
)
$ErrorActionPreference = 'Stop'
$taskBefore = (Get-FileHash -LiteralPath $DatabasePath -Algorithm SHA256).Hash.ToLowerInvariant()
$taskConnection = [System.Data.Odbc.OdbcConnection]::new(
    'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=' + (Resolve-Path -LiteralPath $DatabasePath).Path + ';ReadOnly=1;'
)
$taskExport = [ordered]@{ source_database_sha256 = $taskBefore; method = 'Read-only ODBC SELECT; binary Shape/domain values base64 encoded; no geometry transformation'; tables = [ordered]@{} }
try {
    $taskConnection.Open()
    foreach ($taskName in @('wc46c03lines','wc46c03lines_83','wc46c03polys','wc46c03polys_83','GDB_GeomColumns','GDB_SpatialRefs','GDB_Domains','GDB_CodedDomains')) {
        $taskCommand = $taskConnection.CreateCommand()
        $taskCommand.CommandText = 'SELECT * FROM [' + $taskName + ']'
        $taskReader = $taskCommand.ExecuteReader()
        $taskRows = [System.Collections.Generic.List[object]]::new()
        try {
            while ($taskReader.Read()) {
                $taskRow = [ordered]@{}
                for ($taskIndex = 0; $taskIndex -lt $taskReader.FieldCount; $taskIndex++) {
                    $taskValue = $taskReader.GetValue($taskIndex)
                    if ($taskValue -is [DBNull]) { $taskValue = $null }
                    elseif ($taskValue -is [byte[]]) { $taskValue = @{base64 = [Convert]::ToBase64String($taskValue)} }
                    elseif ($taskValue -is [DateTime]) { $taskValue = $taskValue.ToString('yyyy-MM-ddTHH:mm:ss') }
                    $taskRow[$taskReader.GetName($taskIndex)] = $taskValue
                }
                $taskRows.Add($taskRow)
            }
        } finally { $taskReader.Close() }
        $taskExport.tables[$taskName] = @($taskRows.ToArray())
    }
} finally { $taskConnection.Close() }
$taskAfter = (Get-FileHash -LiteralPath $DatabasePath -Algorithm SHA256).Hash.ToLowerInvariant()
if ($taskBefore -ne $taskAfter) { throw 'Read-only extraction changed source database bytes' }
$taskExport | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $OutputPath -Encoding utf8
Write-Output 'Read-only export completed; source database hash unchanged'
