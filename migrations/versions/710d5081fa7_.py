"""empty message

Revision ID: 710d5081fa7
Revises: None
Create Date: 2014-11-25 22:49:15.570465

"""

# revision identifiers, used by Alembic.
revision = '710d5081fa7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Group',
    sa.Column('Path', sa.String(length=255), nullable=False),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('Path')
    )
    op.create_index(u'ix_Group_Path', 'Group', ['Path'], unique=False)
    op.create_table('File',
    sa.Column('No', sa.Integer(), nullable=False),
    sa.Column('StoredPath', sa.String(length=255), nullable=True),
    sa.Column('MD5Sum', sa.String(length=32), nullable=True),
    sa.Column('SHA1Sum', sa.String(length=40), nullable=True),
    sa.Column('Size', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('No')
    )
    op.create_index(u'ix_File_MD5Sum', 'File', ['MD5Sum'], unique=False)
    op.create_index(u'ix_File_SHA1Sum', 'File', ['SHA1Sum'], unique=False)
    op.create_table('User',
    sa.Column('No', sa.Integer(), nullable=False),
    sa.Column('ID', sa.String(length=255), nullable=True),
    sa.Column('Password', sa.String(length=255), nullable=True),
    sa.Column('APIKey', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('No')
    )
    op.create_table('History',
    sa.Column('No', sa.Integer(), nullable=False),
    sa.Column('Path', sa.String(length=255), nullable=True),
    sa.Column('IP', sa.String(length=255), nullable=True),
    sa.Column('Time', sa.Integer(), nullable=True),
    sa.Column('UserAgent', sa.String(length=255), nullable=True),
    sa.Column('Referrer', sa.String(length=255), nullable=True),
    sa.Column('Country', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('No')
    )
    op.create_index(u'ix_History_Path', 'History', ['Path'], unique=False)
    op.create_table('Path',
    sa.Column('Path', sa.String(length=255), nullable=False),
    sa.Column('ActualName', sa.String(length=255), nullable=True),
    sa.Column('Uploaded', sa.Integer(), nullable=True),
    sa.Column('ExpiresIn', sa.Integer(), nullable=True),
    sa.Column('DownloadLimit', sa.Integer(), nullable=True),
    sa.Column('Downloaded', sa.Integer(), nullable=True),
    sa.Column('GroupPath', sa.String(length=255), nullable=True),
    sa.Column('FileNo', sa.Integer(), nullable=True),
    sa.Column('HideAfterLimitExceeded', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['FileNo'], ['File.No'], ),
    sa.ForeignKeyConstraint(['GroupPath'], ['Group.Path'], ),
    sa.PrimaryKeyConstraint('Path')
    )
    op.create_index(u'ix_Path_GroupPath', 'Path', ['GroupPath'], unique=False)
    op.create_index(u'ix_Path_Path', 'Path', ['Path'], unique=True)
    op.create_index(u'ix_Path_Uploaded', 'Path', ['Uploaded'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_Path_Uploaded', table_name='Path')
    op.drop_index(u'ix_Path_Path', table_name='Path')
    op.drop_index(u'ix_Path_GroupPath', table_name='Path')
    op.drop_table('Path')
    op.drop_index(u'ix_History_Path', table_name='History')
    op.drop_table('History')
    op.drop_table('User')
    op.drop_index(u'ix_File_SHA1Sum', table_name='File')
    op.drop_index(u'ix_File_MD5Sum', table_name='File')
    op.drop_table('File')
    op.drop_index(u'ix_Group_Path', table_name='Group')
    op.drop_table('Group')
    ### end Alembic commands ###
