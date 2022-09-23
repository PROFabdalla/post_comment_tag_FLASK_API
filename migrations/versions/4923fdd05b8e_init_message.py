"""init message

Revision ID: 4923fdd05b8e
Revises: b98692a05991
Create Date: 2022-09-23 20:20:09.413655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4923fdd05b8e'
down_revision = 'b98692a05991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags_comments',
    sa.Column('tag_id', sa.Integer(), nullable=True, Primary_key=True),
    sa.Column('comment_id', sa.Integer(), nullable=True, Primary_key=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags_comments')
    op.drop_table('tags')
    # ### end Alembic commands ###
